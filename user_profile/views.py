from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from accounts.models import User
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def show_profile(request):
    return render(request, 'profile_user.html')


def edit_profile(request, *args, **kwargs):
    context = {}
    if request.POST:
        form_edit = EditProfileForm(request.POST, instance=request.user)
        if form_edit.is_valid:
            form_edit.save()
            return HttpResponseRedirect('/show_profile')
        elif user.is_regular:
            form_edit = EditProfileForm(request.POST, instance=request.user,
                                        initial = {
                                            "name" : updated_profile.name,
                                            "username" : updated.profile.username,
                                            "gender" : updated_profile.gender,
                                            "age" : updated_profile.age,
                                            "email" : updated_profile.email,
                                            "city" : updated_profile.city
                                        })
            context['form_edit'] = form_edit
