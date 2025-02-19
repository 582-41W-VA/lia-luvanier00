from django.urls import reverse
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from datetime import datetime, timedelta
from .models import Role, UserAccount, Team, Player, RegistrationType, Registration, Park, Game, Announcement, Flag, Comment, LikedComment, FavoriteTeam

class WioblAdminArea(admin.AdminSite):
    site_header = 'WIOBL Admin'
    site_url = "/wioblapp/"

    def get_urls(self):
        urls = super().get_urls()
        return urls

    def each_context(self, request):
        context = super().each_context(request)

        if request.path == reverse('admin:index'):
            total_users = UserAccount.objects.count() or 0
            new_users = UserAccount.objects.filter(date_joined__gt=datetime.now() - timedelta(days=7)).count() or 0
            total_registrations = Registration.objects.count() or 0
            new_registrations = Registration.objects.filter(date_time__gt=datetime.now() - timedelta(days=7)).count() or 0
            
            pending_registrations = Registration.objects.filter(team__isnull=True).count()

            unreviewed_flags = 0  

            context.update({
                'total_users': total_users,
                'new_users': new_users,
                'total_registrations': total_registrations,
                'new_registrations': new_registrations,
                'pending_registrations': pending_registrations,
                'unreviewed_flags': unreviewed_flags,
            })

        return context





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
wiobl_site.register(FavoriteTeam)
wiobl_site.register(Player)
wiobl_site.register(RegistrationType)
wiobl_site.register(Registration)
wiobl_site.register(Park)
wiobl_site.register(Game)
wiobl_site.register(Announcement, AnnouncementAdmin)
wiobl_site.register(Flag)
wiobl_site.register(Comment)
wiobl_site.register(LikedComment)