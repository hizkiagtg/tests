from django.urls import path
from buat_sumbangan.views import *

app_name='buat_sumbangan'

urlpatterns = [
    path('add_donasi/', add_donasi, name='add_donasi'),
    path('history/', show_history, name='show_history'),
   # path('lamar/<id>/lamar_flutter', connect_melamar, name = 'connect_melamar'),
]
