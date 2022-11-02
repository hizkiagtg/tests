from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import *
from accounts.models import User
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def show_profile(request):
    return render(request, 'show_profile.html')

@login_required
def edit_profile(request):
    user = request.user
    form_edit = None
    if user.is_regular:
        if request.method == 'POST':
            form_edit = EditProfileFormReg(request.POST, instance=request.user)
            email_exists = User.objects.filter(email=request.POST.get("email")).exists()
            username_exists = User.objects.filter(username=request.POST.get("username")).exists()

            if email_exists:
                messages.error(request, "Email is already used! Use other email.")
            elif username_exists:
                messages.error(request, "Username is already used! Choose other username.")
            elif form_edit.is_valid():
                form_edit.save()
                messages.success(request, "Succesfully Updated Profile!")
                return redirect('for_profile:show_profile')
            else:
                form_edit = EditProfileFormReg(request.POST, instance=request.user,
                initial = {
                "username": form_edit.username,
                "email": form_edit.email,
                "name": form_edit.name,
                "age": form_edit.age,
                "gender": form_edit.gender,
                "city": form_edit.city,
                })

    elif user.is_bank:
        if request.method == 'POST':
            form_edit = EditProfileFormBank(request.POST, instance=request.user)
            email_exists = User.objects.filter(email=request.POST.get("email")).exists()

            if email_exists:
                messages.error(request, "Email is already used! Use other email.")
            elif form_edit.is_valid():
                form_edit.save()
                messages.success(request, "Succesfully Updated Profile!")
                return redirect('for_profile:show_profile')
            else:
                form_edit = EditProfileFormBank(request.POST, instance=request.user,
                initial = {
                "name": form_edit.name,
                "email": form_edit.email,
                "city": form_edit.city,
                "address": form_edit.address,
            })
    return render(request, 'update_profile.html', {'form_edit':form_edit})

# def validate_email(request):
#     email = request.GET.get('email', None)
        
        
