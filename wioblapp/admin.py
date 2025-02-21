from django.urls import reverse
from django.contrib import admin
from django.contrib.admin import AdminSite, SimpleListFilter
from datetime import datetime, timedelta
from .models import (
    Role,
    UserAccount,
    Team,
    Player,
    RegistrationType,
    Registration,
    Park,
    Game,
    Announcement,
    Flag,
    Comment,
    LikedComment,
    FavoriteTeam,
)


class WioblAdminArea(admin.AdminSite):
    site_header = "WIOBL Admin"
    site_url = "/wioblapp/"

    def get_urls(self):
        urls = super().get_urls()
        return urls

    def each_context(self, request):
        context = super().each_context(request)

        if request.path == reverse("admin:index"):
            total_users = UserAccount.objects.count() or 0
            new_users = (
                UserAccount.objects.filter(
                    date_joined__gt=datetime.now() - timedelta(days=7)
                ).count()
                or 0
            )
            total_registrations = Registration.objects.count() or 0
            new_registrations = (
                Registration.objects.filter(
                    date_time__gt=datetime.now() - timedelta(days=7)
                ).count()
                or 0
            )
            pending_registrations = Registration.objects.filter(
                team__isnull=True
            ).count()

            unreviewed_flags = Flag.objects.filter(reviewed=False).count()

            unvalidated_registrations_url = (
                reverse("admin:wioblapp_registration_changelist") + "?validated=False"
            )

            context.update(
                {
                    "total_users": total_users,
                    "new_users": new_users,
                    "total_registrations": total_registrations,
                    "new_registrations": new_registrations,
                    "pending_registrations": pending_registrations,
                    "unreviewed_flags": unreviewed_flags,
                    "unvalidated_registrations_url": unvalidated_registrations_url,
                }
            )

        return context


class ValidatedRegistrationFilter(SimpleListFilter):
    title = "Validated"
    parameter_name = "validated"

    def lookups(self, request, model_admin):
        return (
            ("True", "Validated"),
            ("False", "Unvalidated"),
        )

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(team__isnull=False)
        if self.value() == "False":
            return queryset.filter(team__isnull=True)
        return queryset


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("player", "validated", "reg_type", "team", "date_time")
    list_filter = (ValidatedRegistrationFilter,)

    def validated(self, obj):
        return obj.validated

    validated.boolean = True
    validated.short_description = "Validated"

    def lookups(self, request, model_admin):
        return (
            ("True", "Validated"),
            ("False", "Unvalidated"),
        )

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(team__isnull=False)
        if self.value() == "False":
            return queryset.filter(team__isnull=True)
        return queryset


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("player", "validated", "reg_type", "team", "date_time")
    list_filter = (ValidatedRegistrationFilter,)

    def validated(self, obj):
        return obj.validated

    validated.boolean = True
    validated.short_description = "Validated"


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "user_account")
    list_filter = ("date",)
    exclude = ("user_account",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_account = request.user
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_account", "content", "date", "likes")
    list_filter = ("date",)
    ordering = ("likes",)
    search_fields = ("user_account__username",)
    exclude = (
        "user_account",
        "likes",
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_account = request.user
        super().save_model(request, obj, form, change)

    def get_ordering(self, request):
        ordering = super().get_ordering(request)
        if request.GET.get("o") == "4":
            return ["-likes"]
        return ["likes"]


class FlagAdmin(admin.ModelAdmin):
    list_display = ("comment", "reviewed", "date")
    list_filter = ("reviewed",)
    exclude = ("user_account",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_account = request.user
        super().save_model(request, obj, form, change)


class FavoriteTeamAdmin(admin.ModelAdmin):
    list_display = ("user_account", "team")
    list_filter = ("team",)
    search_fields = ("user_account__username", "team__name")
    exclude = ("user_account",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_account = request.user
        super().save_model(request, obj, form, change)


class GameAdmin(admin.ModelAdmin):
    list_display = (
        "team_1",
        "team_2",
        "date_time",
        "winner",
        "team1_score",
        "team2_score",
        "park",
    )
    list_filter = ("date_time", "winner", "park")
    search_fields = ("team_1__name", "team_2__name", "winner__name", "park__name")
    ordering = ("-date_time",)


class LikedCommentAdmin(admin.ModelAdmin):
    list_display = ("user_account", "comment_preview")
    list_filter = ("user_account",)
    search_fields = ("user_account__username", "comment__content")
    ordering = ("-id",)
    exclude = ("user_account",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_account = request.user
        super().save_model(request, obj, form, change)

    def comment_preview(self, obj):
        return (
            obj.comment.content[:50] + "..."
            if len(obj.comment.content) > 50
            else obj.comment.content
        )

    comment_preview.short_description = "Comment"


class ParkAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "latitude", "longitude")
    search_fields = ("name", "address")
    list_filter = ("name",)
    ordering = ("name",)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "related_account", "team_name", "dob", "gender")
    search_fields = ("name", "related_account__username", "team_name__name")
    list_filter = ("team_name", "gender", "dob")
    ordering = ("name",)


class RegistrationTypeAdmin(admin.ModelAdmin):
    list_display = ("reg_type", "description", "cost")
    search_fields = ("reg_type", "description")
    list_filter = ("cost",)
    ordering = ("reg_type",)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "get_coaches", "place", "group", "color")
    search_fields = ("name", "coaches__username", "group__reg_type")
    list_filter = ("group", "place")
    ordering = ("place", "name")

    def get_coaches(self, obj):
        """Show a list of coaches assigned to the team."""
        return (
            ", ".join([coach.username for coach in obj.coaches.all()])
            if obj.coaches.exists()
            else "No Coaches"
        )

    get_coaches.short_description = "Coaches"


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "phone", "is_active", "is_staff")
    search_fields = ("username", "email", "role__name", "phone")
    list_filter = ("role", "is_active", "is_staff", "is_superuser")
    ordering = ("username",)


wiobl_site = WioblAdminArea(name="WioblAdmin")


wiobl_site.register(Role, RoleAdmin)
wiobl_site.register(UserAccount, UserAccountAdmin)
wiobl_site.register(Team, TeamAdmin)
wiobl_site.register(FavoriteTeam, FavoriteTeamAdmin)
wiobl_site.register(Player, PlayerAdmin)
wiobl_site.register(RegistrationType, RegistrationTypeAdmin)
wiobl_site.register(Registration, RegistrationAdmin)
wiobl_site.register(Park, ParkAdmin)
wiobl_site.register(Game, GameAdmin)
wiobl_site.register(Announcement, AnnouncementAdmin)
wiobl_site.register(LikedComment, LikedCommentAdmin)
wiobl_site.register(Flag, FlagAdmin)
wiobl_site.register(Comment, CommentAdmin)
