from django.db import models

# Create your models here.
class Donasi(models.Model):
   # donatur = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    jenis = models.CharField(max_length=15)
    berat = models.IntegerField(null=True)
    poin = models.IntegerField(null=True)

