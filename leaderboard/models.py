from django.db import models
from accounts.models import *

# Create your models here.
class Leaderboard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #username = models.CharField(max_length = 20, blank = True, null = True, unique = True)
    #email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    name = models.CharField(max_length=50)
    #age = models.IntegerField(null=True)
    #gender = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    address = models.TextField(null=True)
    #score = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)