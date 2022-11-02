from django.urls import path
from forum.views import homePage
from forum.views import questionPage
from forum.views import addQuestion
from forum.views import questionJson



urlpatterns = [
    path('', homePage, name = 'forum'),
    path('question/<int:id>', questionPage, name='question'),
    path('addQuestion/', addQuestion, name='addQuestion'),
    path('json/', questionJson, name='json'),

]