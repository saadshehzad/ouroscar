from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create_partner),
    path("login/", partner_login, name="partner_login"),
    path("password/change", partner_change_password, name="partner_change_password"),
    path("profile", partner_profile, name="partner_profile")
]
