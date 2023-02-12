from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()


def partneraddress_list(request):
    obj = PartnerAddress.objects.all()
    context = {"partners": obj}
    return render(request, "partner/partner_list.html", context)


def creat_partneraddress(request):
    form = PartneraddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("your form has been saved")
    context = {"form": form}
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


def create_partner(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            password = make_password(request.POST.get("password"))
            all_users = User.objects.all()
            for user in all_users:
                if email == user.email:
                    return HttpResponse("User with this email already exists.")
            user = User.objects.create(first_name=first_name,
                last_name=last_name, username=username, email=email,
                password=password)
            Partners.objects.create(user=user, phone=phone)
            return redirect("login")
        except:
            return HttpResponse("Cannot Create partner")
    return render(request, "partner/create_partner.html")


def partner_profile(request):
    partner = Partners.objects.get(user=request.user)
    context = {
        "name": partner.user.first_name,
        "email": partner.user.email
    }
    return render(request, "partner/partner_profile.html", context)