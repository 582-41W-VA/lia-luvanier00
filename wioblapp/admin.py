from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag

class WioblAdminArea(admin.AdminSite):
    site_header = 'WIOBL Admin'
    site_url = "/wioblapp/" 

wiobl_site = WioblAdminArea(name='WioblAdmin')

wiobl_site.register(Role)
wiobl_site.register(UserAccount)
wiobl_site.register(Team)
wiobl_site.register(Player)
wiobl_site.register(RegistrationTypes)
wiobl_site.register(Registration)
wiobl_site.register(Park)
wiobl_site.register(Game)
wiobl_site.register(Comment)
wiobl_site.register(Announcement)
wiobl_site.register(Flag)