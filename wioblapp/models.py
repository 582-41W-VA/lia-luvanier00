from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField("Role", max_length=100, primary_key=True)
    description = models.TextField("Role Description")

    def __str__(self):
        return self.name


class UserAccount(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.RESTRICT,
        related_name="user_accounts",
        null=True,
        blank=True,
    )
    phone = models.CharField("Phone Number", max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class RegistrationType(models.Model):
    reg_type = models.CharField("Registration Type", max_length=50, primary_key=True)
    description = models.CharField("Description", max_length=300)
    cost = models.IntegerField("Cost", validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.reg_type)


class Team(models.Model):
    name = models.CharField("Team Name", max_length=20, primary_key=True)
    coaches = models.ManyToManyField(UserAccount, related_name="teams", blank=True)
    place = models.IntegerField("Place", default=0, validators=[MinValueValidator(0)])
    group = models.ForeignKey(
        RegistrationType,
        on_delete=models.CASCADE,
        related_name="teams",
        blank=True,
        null=True,
    )
    color = models.CharField("Team Color", max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class FavoriteTeam(models.Model):
    user_account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="favoriteteams"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="favoriteteams",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user_account} favorite teams"


class Player(models.Model):
    related_account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="players"
    )
    team_name = models.ForeignKey(
        Team, on_delete=models.RESTRICT, related_name="players", blank=True, null=True
    )
    name = models.CharField("Name", max_length=50)
    dob = models.DateField("Date Of Birth")
    gender = models.CharField("Gender", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="registrations"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="registrations",
    )
    reg_type = models.ForeignKey(
        RegistrationType, on_delete=models.CASCADE, related_name="registrations"
    )
    address = models.CharField("Address", max_length=200)
    email = models.EmailField("Email Address", max_length=254, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=15)
    uniform_size = models.CharField("Uniform Size", max_length=3)
    consent = models.BooleanField("Consent", default=False, null=False)
    volunteer = models.BooleanField("Volunteer", default=False)
    date_time = models.DateTimeField("Date", auto_now_add=True)
    message = models.TextField("Special Requests", blank=True, null=True)

    @property
    def validated(self):
        return self.team is not None

    def __str__(self):
        return f"{self.player} - {self.reg_type}"


class Park(models.Model):
    name = models.CharField("Park Name", max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=20, decimal_places=16, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=16, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    team_1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Team1_games"
    )
    team_2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="Team2_games"
    )
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="games")
    winner = models.ForeignKey(
        Team, on_delete=models.RESTRICT, related_name="games", blank=True, null=True
    )
    date_time = models.DateTimeField("Date")
    team1_score = models.IntegerField(
        "Team #1 Score", validators=[MinValueValidator(0)], blank=True, null=True
    )
    team2_score = models.IntegerField(
        "Team #2 Score", validators=[MinValueValidator(0)], blank=True, null=True
    )

    def __str__(self):
        return f"{self.team_1} / {self.team_2}"


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")
    user_account = models.ForeignKey(
        UserAccount, on_delete=models.RESTRICT, related_name="comments"
    )
    content = models.TextField("Content")
    date = models.DateTimeField("Date", auto_now_add=True)
    likes = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], blank=True, null=True
    )

    def __str__(self):
        return self.content[:20]


class LikedComment(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="likedcomments"
    )
    user_account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="likedcomments"
    )

    def __str__(self):
        return f"{self.user_account} Liked {self.comment.content[:20]}"


class Announcement(models.Model):
    user_account = models.ForeignKey(
        UserAccount, on_delete=models.RESTRICT, related_name="announcements"
    )
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    img_url = models.URLField(blank=True, null=True)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.title


class Flag(models.Model):
    user_account = models.ForeignKey(
        UserAccount, on_delete=models.RESTRICT, related_name="flags"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="flags", blank=True, null=True
    )
    date = models.DateTimeField("Date", auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.comment) if self.comment else "No Comment flagged"
