from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json

from .forms import *

# Create your views here.

def main(request):
    return render(request, "main.html")

def signup(request):
    return render(request, "signup.html")

# Handle sign up form and create User with a spesific role (group).
def regular_signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:main')
    
    if request.method == "POST":
        form = RegularSignUpForm(request.POST)

        username_exists = User.objects.filter(username=request.POST.get("username")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()

        data = {}
    
        if username_exists:
            data['success'] = False
            data['warning'] = "Username has already been used"

        elif email_exists:
            data['success'] = False
            data['warning'] =  "Email has already been used"

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
        return redirect("accounts:main")
    
    if request.method == "POST" and is_ajax:
        form = BankSignUpForm(request.POST)
        name_exists = User.objects.filter(is_bank=True, name=request.POST.get("name")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        data = {}
    
        if name_exists:
            data['success'] = False
            data['warning'] = "Institute name has already been registered"
            
        elif email_exists:
            data['success'] = False
            data['warning'] =  "Email has already been used"
            
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
    # Excecuted when User submit the form.
    if request.method == 'POST':
        # Authenticate User based on username and password.
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        # Executed when User is valid. Redirect to home page.
        if user is not None:
            login(request, user)
            return redirect('accounts:main')

        # Executed when User is not valid. Redirect to login page.
        else:
            messages.success(request, 'There was an error logging In. Please try again!')

    # Rendering login.html.
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('accounts:login'))
    return response

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'