from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag
from .forms import SignUpForm
from django.contrib.auth.models import User

# --------------------------------------------------------------
def index(request):
    announcements = Announcement.objects.order_by("-date")[:3]

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
            user_exist = UserAccount.objects.filter(username=username)
            email = signup_form.cleaned_data.get("email")
            email_exist = UserAccount.objects.filter(email=email)
            password = signup_form.cleaned_data.get("password")
            role = signup_form.cleaned_data.get("role")
            bio = signup_form.cleaned_data.get("bio")

            if user_exist:
                messages.error(request, f"Username {username} is already exist!")
                return render (request, "sign-up.html", {"signup_form": signup_form,})
            
            if email_exist:
                messages.error(request, f"Email {email} is already exist")
                return render (request, "sign-up.html", {"signup_form": signup_form,})


            signup_form.save()
            messages.success(request, "You signed-up successfully")
            member = authenticate(request, username=username, password=password)
            login(request, member)
            return redirect("index")

    context = {
        "signup_form": signup_form,
    }
    return render(request, "sign-up.html", context)
# --------------------------------------------------------------

# --------------------------------------------------------------
def member_login(request):
    login_form = AuthenticationForm()
    
    if request.method == "POST":
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
