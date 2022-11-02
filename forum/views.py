from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseNotFound

@login_required(login_url='accounts:login')
def addQuestion(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        newQuestion = Question(user=request.user, title=title, body = body, date= datetime.now())
        newQuestion .save()
        return HttpResponse(b"CREATED", status=20)
    return HttpResponseNotFound()

@login_required(login_url='accounts:login')
def addAnswer(request):
    if request.method == "POST":
        body = request.POST.get('body')
        newAnsewer = Answer(user=request.user, body = body, date= datetime.now())
        newAnsewer.save()
        return HttpResponse(b"CREATED", status=20)
    return HttpResponseNotFound()

def questionJson(request):
    questions = Question.objects.all()
    return HttpResponse(serializers.serialize('json', questions), content_type='application/json')

def answerJson(request, id):
    answer = Answer.objects.filter(id)
    return HttpResponse(serializers.serialize('json', answer), content_type='application/json')

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'forum.html', context)



