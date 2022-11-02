from django.urls import path
from descriptions.views import *

app_name = 'descriptions'

urlpatterns = [
    path('', desc_json, name='desc_json'),
    path('upload/', show_upload_form, name='show_upload_form'),
    path('add/', upload_desc, name='upload_desc'),
    path('details/<int:id>/', show_details, name='show_details'),
]