from django.forms import forms
from .models import *


class PartneradressForm(forms.Form):
    model = PartnerAddress
    
    fields = "all"