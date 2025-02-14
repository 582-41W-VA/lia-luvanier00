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
class FilterTeamsForm(forms.Form):
    search = forms.CharField(max_length=100, 
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Search team or player'}))

    group = forms.ModelChoiceField(label="Group",
                                   queryset=RegistrationType.objects.all(),
                                   required=True,
                                   widget=forms.Select())

    coach = forms.ModelChoiceField(label="Coach",
                             queryset=UserAccount.objects.filter(role="Coach"),
                             required=False,
                             widget=forms.Select())
# --------------------------------------------------------------

# --------------------------------------------------------------
class TeamScheduleForm(forms.ModelForm):
    MONTH_CHOICES = [
        ("June", "June"),
        ("July", "July"),
        ("August", "August")
    ]

    month = forms.ChoiceField(label="Month", 
                              choices=MONTH_CHOICES,
                              required=False,
                              widget=forms.Select())

    date_time = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Game
        fields = ["month", "date_time", "winner"]
# --------------------------------------------------------------

# --------------------------------------------------------------
class TeamScheduleForm(forms.ModelForm):
    MONTH_CHOICES = [
        ("June", "June"),
        ("July", "July"),
        ("August", "August")
    ]

    month = forms.ChoiceField(label="Month", 
                              choices=MONTH_CHOICES,
                              required=False,
                              widget=forms.Select())

    date_time = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Game
        fields = ["month", "date_time", "winner"]
# --------------------------------------------------------------

# --------------------------------------------------------------
class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':85}))
    class Meta:
        model = Comment
        fields = ['content']
# --------------------------------------------------------------
