from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import UserExtension

# Define an inline admin descriptor for UserExtension model
# which acts a bit like a singleton
class UserExtensionInline(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = 'User'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserExtensionInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)