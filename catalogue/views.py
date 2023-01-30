from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from .models import Category, Product, ProductClass


def product_list(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, "catalogue/product_list.html", context)


def create_product(request):
    product_form = ProductForm(request.POST or None)
    if product_form.is_valid():
        product_form.save()
        return redirect("product_list")
    context = {"form": product_form}
    return render(request, "catalogue/create_product.html", context)


def detail_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return HttpResponse("Product does not exists.")
    context = {"obj": product}
    return render(request, "catalogue/product_detail.html", context)


def update_product(request, id):
    try:
        obj = Product.objects.get(id=id)
    except:
        return HttpResponse("Product does not exists.")

    product_form = ProductForm(request.POST or None, instance=obj)
    if product_form.is_valid():
        product_form.save()
        return redirect("/")
    context = {"form": product_form}
    return render(request, "catalogue/product_update.html", context)


def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return HttpResponse("Product does not exists.")
    if request.method == "POST":
        product.delete()
        return redirect("/")
    context = {"obj": product}
    return render(request, "catalogue/product_delete.html", context)


# Categories CRUD


def categoris_list(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "catalogue/list_category.html", context)


def get_category_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return HttpResponse("Category does not exists.")
    context = {"obj": category}
    return render(request, "catalogue/get_category.html", context)


def create_cateory(request):
    category_form = CategoryForm(request.POST or None)
    if category_form.is_valid():
        category_form.save()
        return redirect("category_list")
    context = {"form": category_form}
    return render(request, "catalogue/create_category.html", context)


def update_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return HttpResponse("Category does not exists")
    category_form = CategoryForm(request.POST or None, instance=category)
    if category_form.is_valid():
        category_form.save()
        return redirect("/")
    context = {"form": category_form}
    return render(request, "catalogue/update_category.html", context)


def delete_category_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return HttpResponse("Category does not exists")
    if request.method == "POST":
        category.delete()
        return redirect("/")
    context = {"obj": category}
    return render(request, "catalogue/delete_category.html", context)


# ProductClass CRUD
def productclass_list(request):
    product_class = ProductClass.objects.all()
    context = {"product_class": product_class}
    return render(request, "catalogue/productclass_list.html", context)


def create_productclass(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {"form": form}
    return render(request, "catalogue/create_productclass.html", context)


def get_productclass(request, id):
    try:
        product_class = ProductClass.objects.get(id=id)
    except:
        return HttpResponse("Product Class Does not exists")
    context = {"obj": product_class}
    return render(request, "catalogue/get_productclass.html", context)


def update_productclass(request, id):
    product_class = ProductClass.objects.get(id=id)
    form = ProductClassForm(request.POST or None, instance=product_class)
    if form.is_valid():
        form.save()
        return redirect("productclass_list")
    context = {"form": form}
    return render(request, "catalogue/update_productclass.html", context)


def delete_productclass(request, id):
    try:
        product_class = ProductClass.objects.get(id=id)
    except:
        return HttpResponse("Product Class Does not exists")
    if request.method == "POST":
        product_class.delete()
        return redirect("/")
    context = {"obj": obj}
    return render(request, "catalogue/delete_productclass.html", context)
