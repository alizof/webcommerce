from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'cgc', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cgc',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)