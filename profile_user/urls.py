from django.urls import path
from profile_user.views import *

app_name = 'profile_user'

urlpatterns = [
    path('show_profile/', show_profile, name = 'show_profile'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
]
