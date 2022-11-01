from django.db import models
from accounts.models import *

# Create your models here.
class Donasi(models.Model):
    donatur = models.ForeignKey(User,on_delete=models.CASCADE, related_name="donatur")
    date = models.DateField()
    jenis = models.CharField(max_length=15)
    berat = models.IntegerField(null=True)
    poin = models.FloatField(null=True)
    bank_sampah = models.CharField(max_length=50)
   