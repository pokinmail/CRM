from django.contrib import admin
from .models import CustomUser, UserTeam
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User profile',
            {
                'fields':(
                    'department',
                    'is_frontstaff',
                    'is_doctor',
                    'is_backstaff',
                    'userteam',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserTeam)

