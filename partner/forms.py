from django import forms
from .models import *


class PartnerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    

class PartnerChangePassword(forms.Form):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    