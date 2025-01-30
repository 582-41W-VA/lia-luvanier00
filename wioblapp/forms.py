from django import forms
from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), 
                                     required=True, 
                                     widget=forms.RadioSelect)

    bio = forms.CharField(max_length=500, widget=forms.Textarea, required=False)

    class Meta:
        model = UserAccount
        fields = ["username", "email", "password1", "password2", "role", "bio"]
