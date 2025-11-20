from django import forms 
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField(required=False)

    class Meta:
       model = User
       fields = ['first_name', 'last_name', 'email','username']

    def clean(self):
       cleaned_data = super().clean()
       p = cleaned_data.get('password')
       cp = cleaned_data.get('confirm_password')

       if p != cp:
        raise forms.ValidationError("Passwords do not match!")
       return cleaned_data