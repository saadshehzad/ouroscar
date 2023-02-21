from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create_partner),
    path("login/", partner_login, name="partner_login"),
    path("profile", partner_profile, name="partner_profile"),
    path("user/create/", user_register_view)
    
]
