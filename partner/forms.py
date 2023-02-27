from django import forms
from .models import *


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields ="__all__"
        
class PartnerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class UserPasswordChange(forms.Form):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class PartnerChangePassword(forms.Form):
    old_password = forms.CharField(max_length=100)
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    