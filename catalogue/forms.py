from django import forms

from .models import *


class ProductForm(forms.ModelForm):    
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {'partner': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['partner'].required = False


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductClassForm(forms.ModelForm):
    class Meta:
        model = ProductClass
        fields = "__all__"
