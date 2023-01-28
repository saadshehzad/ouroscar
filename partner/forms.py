from django.forms import forms
from .models import *


class PartneradressForm(forms.ModelForm):
    model = PartnerAddress
    fields = "__all__"