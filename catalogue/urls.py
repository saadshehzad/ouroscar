from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    # Product urls
    path("products/list/", product_list),
    path("product/create/", create_product),
    path("product/detail/<id>/", detail_product),
    path("product/update/<id>/", update_product),
    path("product/delete/<id>/", delete_product),
    # Category urls
    path("categories/list/", categoris_list),
    path("categories/create/", create_cateory),
    path("categories/get/<int:id>", get_category_by_id),
    path("categories/update/<int:id>", update_category),
    path("categories/delete/<int:id>/", delete_category_by_id),
    # ProductClass urls
    path("productclass/list", productclass_list),
    path("productclass/create/", create_productclass),
    path("productclass/get/<int:id>", get_productclass),
    path("productclass/update/<int:id>", update_productclass),
    path("productclass/delete/<int:id>", delete_productclass),
]
