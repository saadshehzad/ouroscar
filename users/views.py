from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from .forms import *
from .models import *




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

