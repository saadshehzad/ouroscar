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
    # ProductOptions Urls
    path("productoptions/list/", productoptions_list),
    path("productoptions/create/", create_productoptions),
    path("productoptions/get/<int:id>", get_productoptions_by_id),
    path("productoptions/update/<int:id>", update_productoptions_by_id),
    path("productoptions/delete/<int:id>/", delete_productoption_by_id),
]
