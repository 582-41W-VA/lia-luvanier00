from django import forms
from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --------------------------------------------------------------
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
# --------------------------------------------------------------

# --------------------------------------------------------------
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
# --------------------------------------------------------------
 
# --------------------------------------------------------------
class RegistrationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")]
    
    UNIFORM_SIZES = [
        ("", "Select a size"),
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

    uniform_size = forms.ChoiceField(label="Uniform Size", choices=UNIFORM_SIZES, 
                                     required=True, 
                                     widget=forms.Select())
    consent = forms.BooleanField(label="Consent", required=True)
    volunteer = forms.ChoiceField(choices=VOLUNTEER_CHOICES, 
                               required=True, 
                               widget=forms.RadioSelect)

    class Meta:
        model = Registration
        fields = ["firstname", "lastname", "dob", "gender", "group", "street_line1", "app_line2", "city", "province", "postal_code", "country", "email", "phone", "uniform_size", "consent", "volunteer", "message"]
# --------------------------------------------------------------

# --------------------------------------------------------------
class ModifyAccountForm(forms.ModelForm):
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput, required=True)
    phone = forms.CharField(label="Phone Number", required=False)

    class Meta:
        model = UserAccount
        fields = ["username", "first_name", "last_name", "password", "email", "phone", "role"]
# --------------------------------------------------------------

# --------------------------------------------------------------
class FilterTeamsForm(forms.ModelForm):
    SEASON_CHOICES = [
        ("2025", "2025"),
        ("2024", "2024"),
        ("2023", "2023")]

    season = forms.ChoiceField(label="Season",
                               choices=SEASON_CHOICES,
                               required=True,
                               widget=forms.Select())

    group = forms.ModelChoiceField(label="Group",
                              queryset=RegistrationType.objects.all(),
                              required=True,
                              widget=forms.Select())

    # team = forms.ModelChoiceField(label="Team", 
    #                               queryset=Team.objects.all(),
    #                               required=True,
    #                               widget=forms.Select())

    class Meta:
        model = Team
        fields = ["season", "group"]
# --------------------------------------------------------------

# --------------------------------------------------------------
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
# --------------------------------------------------------------
