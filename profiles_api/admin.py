# from django.contrib import admin
# from profiles_api import models  # To import models we created from profiles_api

# admin.site.register(models.UserProfile) # This is telling Django to register UseProfile model with the admin site

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profiles_api import models


class UserProfileAdmin(UserAdmin):
    """Define admin model for custom user model with email instead of username"""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "name", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2"),
            },
        ),
    )


admin.site.register(models.UserProfile, UserProfileAdmin)
