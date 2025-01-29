from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField("Role", max_length=100, primary_key=True)
    description = models.TextField("Role Description")

    def __str__(self):
        return self.name

class UserAccount(User):
    role = models.ForeignKey(Role, on_delete=models.RESTRICT, related_name="user_accounts")
    bio = models.TextField("Bio", blank=True, null=True)
    # username = models.CharField("Username", max_length=100)
    # email = models.EmailField("Email Adress", max_length=254, unique=True)
    # password = models.CharField("Password", max_length=100)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField("Team Name", max_length=20, primary_key=True)
    coaches = models.ManyToManyField(UserAccount, related_name="teams")
    place = models.IntegerField("Place", default=0)

    def __str__(self):
        return self.name

class Player(models.Model):
    related_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="players")
    team_name = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name="players")
    name = models.CharField("Name", max_length=50)
    dob = models.DateField("Date Of Birth")

    def __str__(self):
        return self.name

class RegistrationTypes(models.Model):
    reg_type = models.CharField("Registration Type", max_length=50, primary_key=True)
    description = models.CharField("Description", max_length=300)
    cost = models.IntegerField("Cost")

    def __str__(self):
        return self.reg_type

class Registration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="registrations")
    reg_type = models.ForeignKey(RegistrationTypes, on_delete=models.CASCADE, related_name="registrations")
    date_time = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.reg_type

class Park(models.Model):
    name = models.CharField("Park Name", max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team1_games")
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team2_games")
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="games")
    winner = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name="games", blank=True, null=True)
    date_time = models.DateTimeField("Date")
    team1_score = models.IntegerField("Team #1 Score", blank=True, null=True)
    team2_score = models.IntegerField("Team #2 Score", blank=True, null=True)

    def __str__(self):
        return f"{self.team_1} / {self.team_2}"

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")
    user_account = models.ForeignKey(UserAccount, on_delete=models.RESTRICT, related_name="comments")
    content = models.TextField("Content")
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.content[:20]

class Announcement(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.RESTRICT, related_name="announcements")
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.title

class Flag(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.RESTRICT, related_name="flags")
    flagged_content = models.CharField("Flagged Content", max_length=100)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.flagged_content

