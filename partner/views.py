from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
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
            return redirect("partner_login")
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
    return render(request, "registration/partner_login.html", context)
    


def partner_change_password(request):
    if not request.user.id:
        return HttpResponse("You need to login first")
    if request.method == "POST":
        form = PartnerChangePassword(request.POST or None)
        if form.is_valid():
            partner_ = User.objects.get(id=request.user.id)
            old_password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password"]
            if partner_.check_password(old_password):
                partner_.set_password(new_password)
                partner_.save()
                recipient_list = [request.user.email]
                send_mail("subject", "Your Password has been changed", "ouroscar@point.com",[recipient_list], fail_silently=False)
                return HttpResponse("Your password has been changed succesfully.")
            else:
                return HttpResponse("Your old password is not correct.")
    else:
        form = PartnerChangePassword()
    return render(request, 'registration/partner_change_password.html', {'form': form})



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
            return redirect("user_login")
        except:
            return HttpResponse("Cannot Create partner")
    return render(request, "user/user_create.html")



def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                recipient_list = [request.user.email]
                send_mail("subject", "You are Logged in", "ouroscar@point.com",[recipient_list], fail_silently=False)

                return HttpResponse("logged in")
            else:
                return HttpResponse("Invalide credentials.")
    context = {"form": form}
    return render(request, "registration/user_login.html", context)


def logout_(request):
    if not request.user.is_authenticated:
        return HttpResponse("user already logged out")
    logout(request)
    return HttpResponse("Success Logged out")
    
    
    
def user_change_password(request):
    if not request.user.id:
        return HttpResponse("You need to login first.")
    
    if request.method == 'POST':
        form = UserPasswordChange(request.POST)
        if form.is_valid():
            this_user = User.objects.get(id=request.user.id)
            old_password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password"]
            if this_user.check_password(old_password):
                this_user.set_password(new_password)
                this_user.save()
                recipient_list = [request.user.email]
                send_mail("subject", "Your Password has been changed", "ouroscar@point.com",[recipient_list], fail_silently=False)
                return HttpResponse("Your password has been changed succesfully.")
            else:
                return HttpResponse("Your old password is not correct.")
    else:
        form = UserPasswordChange()
    return render(request, 'registration/change_password.html', {'form': form})

