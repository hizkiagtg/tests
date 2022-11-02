from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'forum'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('get_question/', views.get_question, name='get_question'),

]