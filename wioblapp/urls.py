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
    path("like_team/<str:team_name>/", views.like_team, name="like_team"),
    path("dislike_team/<str:team_name>/", views.dislike_team, name="dislike_team"),
    path("team_schedule/<str:team_name>/", views.team_schedule, name="team_schedule"),
    path( "create-comment/<str:team_name>/", views.create_comment, name="create_comment"),
    path("like-comment/<str:team_name>/", views.like_comment, name="like_comment"),
    path("flag-comment/<str:team_name>/", views.flag_comment, name="flag_comment"),
    path("edit-comment/<str:team_name>/<int:comment_id>/",views.edit_comment,name="edit_comment"),
    path("delete-comment/<str:team_name>/", views.delete_comment, name="delete_comment"),
]
