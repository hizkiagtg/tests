from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', main, name='main'),
    path('signup/', signup, name='signup'),
    path('signup/reg/', regular_signup, name='regular_signup'),
    path('signup/bank/', bank_signup, name='bank_signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]