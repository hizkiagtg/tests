from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', main, name='main'),
    path('regular-signup/', regular_signup, name='regular_signup'),
    path('bank-signup/', bank_signup, name='bank_signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]