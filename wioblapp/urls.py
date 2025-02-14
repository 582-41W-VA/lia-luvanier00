# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.member_login, name="login"),
    path("logout/", views.member_logout, name="logout"),
    path("about/", views.about, name="about"), 
    path("sign-up/", views.sign_up, name="sign-up"),
    path("account/<int:account_id>/", views.member_account, name="member_account"),
    path("registration/", views.register_player, name="registration"),
    path("teams/", views.teams, name="teams"),
    path("team_schedule/<str:team_name>/", views.team_schedule, name="team_schedule"),
    path("create-comment/<str:team_name>/", views.create_comment, name="create_comment"),
    path("like-comment/<str:team_name>/", views.like_comment, name="like_comment"),
    path("flag-comment/<str:team_name>/", views.flag_comment, name="flag_comment"),
]
