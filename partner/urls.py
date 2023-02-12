from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create_partner),
    path("profile", partner_profile, name="profile")
]
