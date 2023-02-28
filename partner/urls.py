from django.urls import path

from .views import *

urlpatterns = [
    # urls of Partner
    path("create/", create_partner),
    path("login/", partner_login, name="partner_login"),
    path("password/change", partner_change_password, name="partner_change_password"),
    path("profile", partner_profile, name="partner_profile"),
    
    #urls of User
    path("user/create/", user_register_view),
    path("user/login/", user_login, name="user_login"),
    path("logout/", logout_, name="user_logout"),
    path("user/password/change", user_change_password, name="user_change_password")
    
]
