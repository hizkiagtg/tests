from django import forms
from accounts.models import User

class EditProfileFormReg(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'gender', 'city']

class EditProfileFormBank(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email','city', 'address']

        # def clean_email(self):
        #     email = self.clened_data.get('email')
            

        # def save_profile(self, commit=True):
        #     updated_profile = super(EditProfileForm, self).save(commit=False)
        #     updated_profile.email = self.cleaned_data['email']
        #     if commit:
        #         updated_profile.save()
        #     return updated_profile
        


