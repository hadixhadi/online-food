from django import forms
from .models import *
class UserRegisterFrom(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

    def clean(self):
        cleaned_data = super(UserRegisterFrom, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email=cleaned_data.get('email')
        if password1 != password2:
            raise forms.ValidationError(
                "Password does not match!"
            )
        if len(email) > 200:    
            raise forms.ValidationError(
                "this email is too long!"
            )