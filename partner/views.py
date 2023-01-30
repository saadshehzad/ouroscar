from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *


def partneraddress_list(request):
    obj = PartnerAddress.objects.all()
    print(obj)
    context = {"partners": obj}
    return render(request, "partner/partner_list.html", context)


def creat_partneraddress(request):
    form = PartneraddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("your form has been saved")
    context = {"form":form}
    return render(request, "partner/partner_create.html", context)

def partneraddress_detail(request, id):
    try:
        obj = PartnerAddress.objects.get(id=id)
    except:
        return HttpResponse("Address Not Available")
    context = {"obj": obj}
    return render(request, "partner/partner_detail.html", context)


def partneraddress_update(request, id):
    try:
        obj = PartnerAddress.objects.get(id=id)
        form = PartneraddressForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/")
    except:
        return HttpResponse("Address is Not Available")
    context = {"form": form}
    return render(request, "partner/partner_update.html", context)


def delete_partneraddress(request, id):
    try:
        obj = PartnerAddress.objects.get(id=id)
        if request.method == "POST":
            obj.delete()
            return redirect("/")
    except:
        return HttpResponse("Address is Not Available")
    context = {"obj": obj}
    return render(request, "partner/delete_partner.html", context)