from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post


class CoreBaseAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Post)
class PostAdmin(CoreBaseAdmin):

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            if not instance.owner:
                instance.owner = request.user.companyemployee
            instance.save()

        super().save_formset(request, form, formset, change)

    def has_change_permission(self, request, obj=None):
        if request.user.role == 'admin':
            return True


@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "role")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "role")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email", "role")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )





