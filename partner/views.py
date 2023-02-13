from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import *


def create_partner(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            password = make_password(request.POST.get("password"))
            all_users = User.objects.all()
            for user in all_users:
                if email == user.email:
                    return HttpResponse("User with this email already exists.")
            user = User.objects.create(first_name=first_name,
                last_name=last_name, username=username, email=email,
                password=password)
            Partners.objects.create(user=user, phone=phone, address=address)
            return redirect("login")
        except:
            return HttpResponse("Cannot Create partner")
    return render(request, "partner/create_partner.html")


def partner_profile(request):
    partner = Partners.objects.get(user=request.user)
    context = {
        "name": partner.user.first_name,
        "email": partner.user.email,
        "address": partner.address
    }
    return render(request, "partner/partner_profile.html", context)
