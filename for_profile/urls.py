from django.urls import path
from for_profile.views import *

app_name = 'for_profile'

urlpatterns = [
    path('show_profile/', show_profile, name = 'show_profile'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
]
