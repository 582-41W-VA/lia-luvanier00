from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.member_login, name="login"),
    path("logout/", views.member_logout, name="logout"),
    path("sign-up/", views.sign_up, name="sign-up"),
]

admin.site.index_title = "West Island Outdoor Basketball League"
admin.site.site_header = "W.I.O.B.L Admin"
admin.site.site_title = "W.I.O.B.L"

