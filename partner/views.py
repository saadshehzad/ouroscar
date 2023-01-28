from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *


def PartnerAdress_list(request):
    obj = PartnerAddress.objects.all()
    print(obj)
    context = {"partners": obj}
    return render(request, "partner_list.html", context)


def creat_partner(request):
    form = PartneradressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("your form has been saved")
    context = {"form":form}
    return render(request, "partner_create.html", context)