from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create_partner),
    path("login/", partner_login, name="partner_login"),
    path("profile", partner_profile, name="partner_profile"),
    path("user/create/", user_register_view),
    path("user/login/", user_login, name="user_login"),
    path("logout/", logout_, name="user_logout"),
    path("password/change", user_change_password, name="user_change_password")
    
]
