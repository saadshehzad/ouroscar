from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
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


def partner_login(request):
    form = PartnerLoginForm()
    if request.method == "POST":
        form = PartnerLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("partner_profile")
            else:
                return HttpResponse("Invalide credentials.")
    context = {"form": form}
    return render(request, "registration/login.html", context)
    


def partner_profile(request):
    partner = Partners.objects.get(user=request.user)
    context = {
        "name": partner.user.first_name,
        "lastname": partner.user.last_name,
        "username": partner.user.username,
        "email": partner.user.email,
        "address": partner.address,
        "phone": partner.phone,
    }
    return render(request, "partner/partner_profile.html", context)



def user_register_view(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = make_password(request.POST.get("password"))
            all_users = User.objects.all()
            for user in all_users:
                if email == user.email:
                    return HttpResponse("User with this email already exists.")
            user = User.objects.create(first_name=first_name,
                last_name=last_name, username=username, email=email,
                password=password)
            # Partners.objects.create(user=user,) We do not need that while creating normal user
            return redirect("login")
        except:
            return HttpResponse("Cannot Create partner")
    return render(request, "partner/create_partner.html")

