from django.shortcuts import redirect, render

from .forms import *
from .models import Category, Product, ProductClass, ProductOptions


def product_list(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, "list.html", context)


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


# ProductOptions CRUD


def productoptions_list(request):
    all_products = ProductOptions.objects.all()
    context = {"productoptions": all_products}
    return render(request, "productoptions_list.html", context)


def create_productoptions(request):
    form = ProductOptionsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("productoptions_list")
    context = {"form": form}
    return render(request, "create_productoptions.html", context)


def get_productoptions_by_id(request, id):
    obj = ProductOptions.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "get_productoptions.html", context)


def update_productoptions_by_id(request, id):
    productoption = ProductOptions.objects.get(id=id)
    form = ProductOptionsForm(request.POST or None, instance=productoption)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form}
    return render(request, "update_productoption.html", context)


def delete_productoption_by_id(request, id):
    obj = ProductOptions.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"obj": obj}
    return render(request, "delete_productoption.html", context)
