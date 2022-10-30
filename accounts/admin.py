from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email','username','is_admin','is_staff', 'is_regular', 'is_bank','weight','score','id',)
    search_fields = ('email','username', 'name')
    readonly_fields = ('id',)
    add_fieldsets = (
        (None, {
            'fields': ('name', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_admin', 'gender', 'city', 'address')}
        ),
    )
    fieldsets = (
    (None, {'fields': ('name', 'password', 'username', 'is_regular', 'is_bank', 'gender', 'city', 'address', 'weight', 'score')}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    (_('Groups'), {'fields': ('groups',)}),
)
    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'city', 'email','username','is_admin','is_staff', 'is_regular', 'is_bank', 'gender')
    #     }),
    #     # ('Advanced options', {
    #     #     'classes': ('collapse',),
    #     #     'fields': ('registration_required', 'template_name'),
    #     # }),
    # )
    # list_display = ('name', 'city', 'email','username','is_admin','is_staff', 'is_regular', 'is_bank', 'gender')
    # search_fields = ('email','username',)
    
admin.site.register(User, CustomUserAdmin) 