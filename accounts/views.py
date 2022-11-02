from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json
import datetime

from .forms import *

# Create your views here.

def main(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse('leaderboard:home_user_login'))
    else:
        return HttpResponseRedirect(reverse('accounts:login'))
    

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('leaderboard:home_user_login'))
    return render(request, "signup.html")

# Handle sign up form and create User with a spesific role (group).
def regular_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('leaderboard:home_user_login'))
    
    if request.method == "POST":
        form = RegularSignUpForm(request.POST)

        username_exists = User.objects.filter(username=request.POST.get("username")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()

        data = {}

        if '@' in request.POST.get("username"):
            data['success'] = False
            data['warning'] = "Username can not contain @."
    
        elif username_exists:
            data['success'] = False
            data['warning'] = "Username has already been used."

        elif email_exists:
            data['success'] = False
            data['warning'] = "Email has already been used."

        else:
            if form.is_valid():
                data['success'] = True
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.is_regular = True
                user.save()

            else:
                data['error'] = form.errors
                data['success'] = False
                context = {"form": form}

        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response        

    form = RegularSignUpForm()
    context = {"form": form}

    return render(request, 'signup.html', context)

def bank_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('leaderboard:home_user_login'))
    
    if request.method == "POST" and is_ajax:
        form = BankSignUpForm(request.POST)
        name_exists = User.objects.filter(is_bank=True, name=request.POST.get("name")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        data = {}
    
        if name_exists:
            data['success'] = False
            data['warning'] = "Institute name has already been registered."
            
        elif email_exists:
            data['success'] = False
            data['warning'] =  "Email has already been used."
            
        else:
            if form.is_valid():
                data['success'] = True
                user = form.save(commit=False)
                user.is_bank = True
                user.save()
                
            else:
                data['error'] = form.errors
                data['success'] = False
                context = {"form": form}
                
        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response

    form = BankSignUpForm()
    context = {"form": form}

    return render(request, "signup.html", context)

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('leaderboard:home_user_login'))

    if request.method == 'POST':
        user_input = request.POST['email']

        try:
            email = User.objects.get(username=user_input).email
        except User.DoesNotExist:
            email = request.POST['email']

        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            response = redirect('leaderboard:home_user_login')
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response

        else:
            messages.success(request, 'Invalid login. Please try again!')

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('accounts:login'))
    response.delete_cookie('last_login')
    request.session.flush()
    return response

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'