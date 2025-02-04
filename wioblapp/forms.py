from django import forms
from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(label="First Name", max_length=50)
    lastname = forms.CharField(label="Last Name", max_length=50)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), 
                                     required=True, 
                                     widget=forms.RadioSelect)
    bio = forms.CharField(max_length=500, widget=forms.Textarea(), required=False)

    class Meta:
        model = UserAccount
        fields = ["firstname", "lastname", "email", "password1", "password2", "role", "bio"]

class RegistrationForm(forms.Form):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")]
    
    UNIFORM_SIZES = [
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "Double Extra Large"),
    ]

    VOLUNTEER_CHOICES = [
        ("True", "Yes"),
        ("False", "No")]

    firstname = forms.CharField(label="First Name", max_length=20)
    lastname = forms.CharField(label="Last Name", max_length=20)
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, 
                               required=True, 
                               widget=forms.RadioSelect)
    group = forms.ModelChoiceField(label="Group Selection", queryset=RegistrationType.objects.all(), 
                                     required=True, 
                                     widget=forms.RadioSelect)
    street_line1 = forms.CharField(label="Street Address", max_length=20)
    app_line2 = forms.CharField(label="Street Address Line 2", max_length=20, required=False)
    city = forms.CharField(label="City", max_length=20)
    province = forms.CharField(label="Province", max_length=20)
    postal_code = forms.CharField(label="Postal Code", max_length=20)
    country = forms.CharField(label="Country", max_length=20)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number")
    uniform_size = forms.ChoiceField(label="Uniform Size", choices=UNIFORM_SIZES, 
                                     required=True, 
                                     widget=forms.Select())
    consent = forms.BooleanField(label="Consent")
    volunteer = forms.ChoiceField(choices=VOLUNTEER_CHOICES, 
                               required=True, 
                               widget=forms.RadioSelect)
    message = forms.CharField(label="Special Requests", widget=forms.Textarea(), required=False)  
