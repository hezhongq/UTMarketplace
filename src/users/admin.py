from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserExtension, EmailVerifyRecord, Listing, Category


# Re-register UserAdmin
class CustomUserAdmin(UserAdmin):
    model = UserExtension
    list_display = ['email', 'username']


class EmailCodesAdmin(admin.ModelAdmin):
    list_display = ('email', 'send_type',)


admin.site.register(UserExtension, CustomUserAdmin)
admin.site.register(EmailVerifyRecord, EmailCodesAdmin)
admin.site.register(Listing)
admin.site.register(Category)
