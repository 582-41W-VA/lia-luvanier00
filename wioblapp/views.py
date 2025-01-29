from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag
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