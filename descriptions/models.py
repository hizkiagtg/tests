from django.db import models
from accounts.models import *

# Create your models here.
class Description(models.Model):
    waste_bank = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='desc-images/')
    description = models.TextField()