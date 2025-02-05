# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.member_login, name="login"),
    path("logout/", views.member_logout, name="logout"),
    path("about/", views.about, name="about"), 
    path("sign-up/", views.sign_up, name="sign-up"),
    path("<int:account_id>/account/", views.member_account, name="member_account"),
    path("registration/", views.register_player, name="registration"),
]
