from django.urls import path

from .views import *

urlpatterns = [
    path("address/list/", partneraddress_list, name="list"),
    path("address/create/", creat_partneraddress),
    path("address/detail/<int:id>", partneraddress_detail),
    path("address/update/<int:id>", partneraddress_update),
    path("address/delete/<int:id>", delete_partneraddress),
    
    # partner
    path("create/", create_partner),
]
