from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag
from .forms import SignUpForm, RegistrationForm
# from django.contrib.auth.models import User

# --------------------------------------------------------------
def index(request):
    announcements = Announcement.objects.order_by("-date")[:4]

    context = {
        "announcements": announcements,
    }
    return render(request, "index.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def sign_up(request):
    signup_form = SignUpForm()

    if request.method == "POST":
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            # firstname = signup_form.cleaned_data.get("firstname").strip()
            # lastname = signup_form.cleaned_data.get("lastname").strip()
            # username = f"{firstname}{lastname}"
            username = signup_form.cleaned_data.get("username")
            email = signup_form.cleaned_data.get("email")
            password = signup_form.cleaned_data.get("password1")
            role = signup_form.cleaned_data.get("role")
            bio = signup_form.cleaned_data.get("bio")

            if UserAccount.objects.filter(username=username).exists():
                messages.error(request, f"Username {username} is already exist!")
                return render (request, "sign-up.html", {"signup_form": signup_form,})
            
            if UserAccount.objects.filter(email=email).exists():
                messages.error(request, f"Email {email} is already exist")
                return render (request, "sign-up.html", {"signup_form": signup_form,})

            member = signup_form.save(commit=False)

            if role == "Admin" or role == "Coach":
                member.is_staff = True
                member.is_superuser = True

            member.save()
            messages.success(request, "You signed-up successfully")
            auth_member = authenticate(request, username=username, password=password)
            if auth_member:
                login(request, auth_member)
                return redirect("index")

    context = {
        "signup_form": signup_form,
    }
    return render(request, "sign-up.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def member_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    login_form = AuthenticationForm()

    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            member = authenticate(request, username=username, password=password)

            if member is not None:
                login(request, member)
                return redirect("index")
            else:
                messages.error(request, "Username OR Password is incorrect!")

    context = {
        "login_form": login_form,
    }
    return render(request, "login.html", context)
# --------------------------------------------------------------

@login_required(login_url="login")
def register_player(request):
    register_form = RegistrationForm()

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)

        if register_form.is_valid():
            firstname = register_form.cleaned_data["firstname"]
            lastname = register_form.cleaned_data["lastname"]
            playername = f"{firstname} {lastname}"
            dob = register_form.cleaned_data["dob"]
            gender = register_form.cleaned_data["gender"]
            group = register_form.cleaned_data["group"]
            email = register_form.cleaned_data["email"]
            phone = register_form.cleaned_data["phone"]
            message = register_form.cleaned_data["message"]

            member = UserAccount.objects.get(email=request.user.email)

            player, created = Player.objects.get_or_create(
                related_account=member,
                name=playername,
                dob=dob,
                gender=gender
            )

            registration = Registration.objects.create(
                player=player,
                reg_type=group,
                email=email,
                phone=phone,
                message=message,
            )

            messages.success(request, "Registration submitted successfully")
            return redirect('index') 

    context = {
        "register_form": register_form,
    }
    return render(request, "registration.html", context)

# --------------------------------------------------------------
@login_required(login_url="login")
def member_logout(request):
    logout(request)
    return redirect("login")
# --------------------------------------------------------------
