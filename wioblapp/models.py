from django.db import models

class Account(models.Model):
    username = models.CharField("Username", max_length=100)
    email = models.EmailField("Email Adress", max_length=254, unique=True)
    password = models.CharField("Password", max_length=100)

    def __str__(self):
        return self.username

class Admin(Account):
    pass
    # account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="admin")

class Coach(Account):
    details = models.TextField("Details")
    # account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="coach")

    def __str__(self):
        return self.account.username

class Team(models.Model):
    name = models.CharField("Team Name", max_length=20)
    coaches = models.ManyToManyField(Coach, related_name="team")
    place = models.IntegerField("Place", default=0)

    def __str__(self):
        return self.name

class Registeration(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Description", max_length=300)
    amount = models.IntegerField("Amount")

    def __str__(self):
        return self.title

class Parent(Account):
    balance = models.IntegerField("Balance", default=0)
    # account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="parent")

    def __str__(self):
        return self.account.username

class Player(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="player")
    team = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name="player")
    registeration = models.ForeignKey(Registeration, on_delete=models.CASCADE, related_name="player")
    name = models.CharField("Name", max_length=50)
    dob = models.DateField("Date Of Birth")

    def __str__(self):
        return self.name

class Park(models.Model):
    name = models.CharField("Park Name", max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="game")
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="game")
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name="game")
    winner = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name="game", blank=True, null=True)
    date_time = models.DateTimeField("Date")
    score = models.CharField("Final Score", blank=True, null=True)

    def __str__(self):
        return f"{self.team_1} / {self.team_2}"

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comment")
    parent = models.ForeignKey(Parent, on_delete=models.RESTRICT, related_name="comment")
    content = models.TextField("Content")
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.content[:20]

class Announcement(models.Model):
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name="announcement")
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.title

class Flag(models.Model):
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name="flag")
    flaged_content = models.CharField("Flaged Content", max_length=100)
    value = models.BooleanField(default=False)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.flaged_content

