from django import forms
from descriptions.models import *

class UploadDesc(forms.ModelForm):
    class Meta:
        model = Description
        exclude = ['waste_bank']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 2}),
        }