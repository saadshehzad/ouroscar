from django.contrib import admin

from .models import ProductClass, Category, Product


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'image')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('product_class',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'category',
        'name',
        'cost',
    )
    list_filter = ('created_at', 'updated_at', 'category')
    search_fields = ('name',)
    date_hierarchy = 'created_at'