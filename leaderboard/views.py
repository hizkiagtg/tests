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
from .models import Leaderboard
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from accounts.models import *
from leaderboard.models import *
from buat_sumbangan.models import *

from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    return render(request, 'user_non.html')

@login_required
def home_user_login(request):
    user = request.user

    if user.is_regular:
        return render(request, 'user_login.html')
    elif user.is_bank:
        return render(request, 'user_bank.html')

def all_json(request):
    user = User.objects.all()
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')

def user_json(request):
    user = User.objects.filter(is_regular=True)
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')

def data_json(request):
    data = User.objects.filter(is_bank=True)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_sorted(request):
    sort = User.objects.filter(is_regular=True).order_by('-weight').only()
    return HttpResponse(serializers.serialize('json', sort), content_type='application/json')

def show_leaderboard(request):
    data_user = Leaderboard.objects.all()
    context = {
        'list_user': data_user,
    }
    return render(request, "leaderboard.html",context)



