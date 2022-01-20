import imp
from webbrowser import BaseBrowser
from django.contrib import admin

"""in this file ı need to import default django user admin and 
i need to change some of the class variablet to support my custom user admin"""

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (('Personal Info'), {'fields': ('name',)}),
    (
        ('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),
    )




admin.site.register(models.User, UserAdmin)