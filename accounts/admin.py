from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email','username','is_admin','is_staff', 'is_regular', 'is_bank','weight','score','id')
    search_fields = ('email','username',)
    readonly_fields = ('id',)
    add_fieldsets = (
        (None, {
            'fields': ('name', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_admin', 'gender', 'city', 'address')}
        ),
    )
    list_display = ('name', 'city', 'email','username','is_admin','is_staff', 'is_regular', 'is_bank', 'gender')
    search_fields = ('email','username',)
    
admin.site.register(User, CustomUserAdmin) 