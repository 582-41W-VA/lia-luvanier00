from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag
from .forms import SignUpForm
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

            if role == "Admin":
                member.is_staff = True
                member.is_superuser = True
            elif role == "Coach":
                member.is_staff = True

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

# --------------------------------------------------------------
@login_required(login_url="login")
def member_logout(request):
    logout(request)
    return redirect("login")
# --------------------------------------------------------------
def about(request):
    return render(request, "about.html")
# --------------------------------------------------------------