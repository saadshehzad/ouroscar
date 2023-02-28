from django.urls import path

from .views import *


urlpatterns = [
    path("create/", user_register_view),
    path("login/", user_login, name="user_login"),
    path("logout/", logout_, name="user_logout"),
    path("change/password", user_change_password, name="user_change_password")
    
    
]
