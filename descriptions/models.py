from django.db import models
from django import forms
from accounts.models import *

# Create your models here.
class Description(models.Model):
    waste_bank = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='desc-images/')
    description = models.TextField()

class UploadDesc(forms.ModelForm):
    class Meta:
        model = Description
        exclude = ['waste_bank']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }