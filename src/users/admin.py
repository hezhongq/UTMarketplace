from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserExtension


# Re-register UserAdmin
class CustomUserAdmin(UserAdmin):
    model = UserExtension
    list_display = ['email', 'username']


admin.site.register(UserExtension, CustomUserAdmin)
