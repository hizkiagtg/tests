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
    
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active')}),
    # )

admin.site.register(User, CustomUserAdmin)


# class RegularUserAdmin(UserAdmin):
#     add_form = RegularSignUpForm
#     model = Regular
#     list_display = ["email", "username",]

# admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(User)
# admin.site.register(Regular)
# admin.site.register(Bank)