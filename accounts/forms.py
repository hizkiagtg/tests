from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email", 
            "password1", 
            "password2", 
        )

class RegularSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name", 
            "email", 
            "username", 
            "password1", 
            "password2", 
            "age", 
            "gender", 
            "city")
        
class BankSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name", 
            "email", 
            "password1", 
            "password2", 
            "city", 
            "address")