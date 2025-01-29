from django.contrib import admin

from .models import Role, UserAccount, Team, Player, RegistrationTypes, Registration, Park, Game, Comment, Announcement, Flag

admin.site.register(Role)
admin.site.register(UserAccount)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(RegistrationTypes)
admin.site.register(Registration)
admin.site.register(Park)
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Announcement)
admin.site.register(Flag)