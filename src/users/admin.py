from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserExtension, EmailVerifyRecord, UserReview, Report
from listings.models import Listing, Bookmark, Category


# Re-register UserAdmin
class CustomUserAdmin(UserAdmin):
    model = UserExtension
    list_display = ['email', 'username', 'avatar', 'rate']
    fieldsets = (  
        (None, {'fields': ('email', 'password', 'username', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  
    )  


class EmailCodesAdmin(admin.ModelAdmin):
    list_display = ('email', 'send_type',)

class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rate',)


admin.site.register(UserExtension, CustomUserAdmin)
admin.site.register(EmailVerifyRecord, EmailCodesAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(Listing)
admin.site.register(Bookmark)
admin.site.register(Category)
admin.site.register(Report)
