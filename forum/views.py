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
        return HttpResponse(serializers.serialize("json",[newQuestion]), content_type="application/json")
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


def answerJson(request):
    answer = Answer.objects.all()

    return HttpResponse(serializers.serialize('json', answer), content_type='application/json')

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'forum.html', context)

"""
@login_required(login_url='accounts:login')
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

"""

