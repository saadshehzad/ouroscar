from django.shortcuts import redirect, render

from .forms import *
from .models import Category, Product, ProductClass


def product_list(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, "product_list.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {"form": form}
    return render(request, "create.html", context)


def detail_product(request, id):
    obj = Product.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "detail.html", context)


def update_product(request, id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form}
    return render(request, "update.html", context)


def delete_product(request, id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"obj": obj}
    return render(request, "delete.html", context)


# Categories CRUD


def categoris_list(request):
    all_categories = Category.objects.all()
    context = {"categories": all_categories}
    return render(request, "list_category.html", context)


def get_category_by_id(request, id):
    obj = Category.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "get_category.html", context)


def create_cateory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    context = {"form": form}
    return render(request, "create_category.html", context)


def update_category(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form}
    return render(request, "update_category.html", context)


def delete_category_by_id(request, id):
    obj = Category.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"obj": obj}
    return render(request, "delete_category.html", context)

# ProductClass CRUD
def productclass_list(request):
    all_productclass = ProductClass.objects.all()
    context = {"products": all_productclass}
    return render(request, "productclass_list.html", context)


def create_productclass(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    context = {"form": form}
    return render(request, "create_productclass.html", context) 


def get_productclass(request, id):
    obj = ProductClass.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "get_productclass.html", context)


def update_productclass(request, id):
    productclass = ProductClass.objects.get(id=id)
    form = ProductClassForm(request.POST or None, instance=productclass)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form}
    return render(request, "update_productclass.html", context)


def delete_productclass(request, id):
    obj = ProductClass.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"obj": obj}
    return render(request, "delete_productclass.html", context )


