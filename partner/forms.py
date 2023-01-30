from django import forms

from .models import *


class PartneraddressForm(forms.ModelForm):
    class Meta:
        model = PartnerAddress
        fields = "__all__"
