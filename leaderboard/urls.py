from django.urls import path
from leaderboard.views import *
from .views import data_json

app_name='leaderboard'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('user/', home_user_login, name='home_user_login'),
    path('data_json/', data_json, name='data_json'),
    path('user_json/', user_json, name='user_json'),
    path('show_json_sorted/', show_json_sorted, name='show_json_sorted'),
    path('leaderboard/', show_leaderboard, name='show_leaderboard'),
]