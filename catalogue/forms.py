from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductOptionsForm(forms.ModelForm):
    class Meta:
        model = ProductOptions
        fields = "__all__"
