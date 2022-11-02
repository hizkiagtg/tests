from tukarpoin.views import *
from django.urls import path


app_name = 'tukarpoin'

urlpatterns = [
    path('', tukarpoin, name='tukarpoin'),
    path('add/', addvoucher, name='add'),
    path('mine/', myvoucher, name='mine'),
    path('json/', get_json, name='get_json'),
    path('added/', createvoucher, name='createvoucher'),
    path('redeem/<int:id>', redeem, name='redeem'),
]