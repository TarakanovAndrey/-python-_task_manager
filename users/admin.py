from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = [
        'first_name',
        'last_name',
        'password',
        'username'
                    ]


admin.site.register(CustomUser, CustomUserAdmin)
