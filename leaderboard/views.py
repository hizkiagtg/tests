import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from models import Leaderboard
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse

from django.views.decorators.csrf import csrf_exempt

#@login_required(login_url='/todolist/login/')
def data_json(request):
    #perlu pake request.user gasi
    data = Leaderboard.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')