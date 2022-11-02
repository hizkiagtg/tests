from django.urls import path
from forum.views import homePage
from forum.views import addQuestion
from forum.views import addAnswer
from forum.views import questionJson
from forum.views import answerJson

urlpatterns = [
    path('', homePage, name = 'forum'),
    path('addQuestion/', addQuestion, name='addQuestion'),
    path('addAnswer/', addAnswer, name='addAnswer'),
    path('json/', questionJson, name='json'),
    path('answerJson/', answerJson, name='answerJson'),

]