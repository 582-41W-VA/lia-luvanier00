from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Comment, Announcement, Flag

class WioblAdminArea(admin.AdminSite):
    site_header = 'WIOBL Admin'
    site_url = "/wioblapp/" 

wiobl_site = WioblAdminArea(name='WioblAdmin')

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "user_account") 
    exclude = ("user_account",) 

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.user_account = request.user
        super().save_model(request, obj, form, change)



wiobl_site.register(Role)
wiobl_site.register(UserAccount)
wiobl_site.register(Team)
wiobl_site.register(Player)
wiobl_site.register(RegistrationType)
wiobl_site.register(Registration)
wiobl_site.register(Park)
wiobl_site.register(Game)
wiobl_site.register(Comment)
wiobl_site.register(Announcement, AnnouncementAdmin)
wiobl_site.register(Flag)