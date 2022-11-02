from django import forms
from accounts.models import User

class EditProfileFormReg(forms.ModelForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'gender', 'city']




class EditProfileFormBank(forms.ModelForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['name', 'email','city', 'address']

            

    # def save_profile(self, commit=True):
    #     updated_profile = super(EditProfileFormBank, self).save(commit=False)
    #     updated_profile.email = self.cleaned_data['email']
    #     if commit:
    #         updated_profile.save()
    #     return updated_profile
        


