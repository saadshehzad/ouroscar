from django.shortcuts import render

from catalogue.models import *


def dashboard(request):
    product = Product.objects.all().count()
    category = Category.objects.all().count()
    context = {"product": product, "category": category}
    return render(request, "catalogue/dashboard.html", context)
