from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from forum.forms import  NewResponseForm, NewReplyForm
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseNotFound


def addQuestion(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        newQuestion = Question(user=request.user, title=title, body = body, date=datetime.now())
        Question.save()
        return HttpResponse(b"CREATED", status=20)
    return HttpResponseNotFound()

def get_question(request):
    questions = Question.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', questions), content_type='application/json')

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'forum.html', context)

def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()
    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    return render(request, 'question.html', context)


#@login_required(login_url='register')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')