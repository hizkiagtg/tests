from django import forms
from accounts.models import User

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'gender', 'city', 'address']

        def clean_email(self):
            email = self.clened_data.get('email')
            

        def save_profile(self, commit=True):
            updated_profile = super(EditProfileForm, self).save(commit=False)
            updated_profile.email = self.cleaned_data['email']
            if commit:
                updated_profile.save()
            return updated_profile
        


