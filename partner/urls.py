from django.urls import path

from .views import *

urlpatterns = [
    path("list/", partneraddress_list),
    path("create/", creat_partneraddress),
    path("detail/<int:id>", partneraddress_detail),
    path("update/<int:id>", partneraddress_update),
    path("delete/<int:id>", delete_partneraddress),
]
