from django.http import HttpRequest
from django.shortcuts import redirect, render

from categories.models import Category
from .models import Product
from .forms import AddProductForm


def show_product_list_page(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  products = Product.objects.all()
  return render(request, 'product-list.html', {
    'products': products
  })
  

def add_product(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')

  if request.method == "GET":
    return show_add_product_page(request)

  form = AddProductForm(request.POST)
  if form.is_valid():
    name = form.cleaned_data['name']
    price = form.cleaned_data['price']
    category_id = form.cleaned_data['category'].id

    if name is None or name == "" or price is None or float(price) < 1:
      return show_add_product_page(request, error='Invalid values')

    category = Category.objects.filter(id=category_id).first()
    if category is None:
      return show_add_product_page(request, error='Category doesn\'t exist')

    form.save()
    return redirect('list-products')


def show_add_product_page(request: HttpRequest, error: str = ""):
  categories = Category.objects.all()
  form = AddProductForm()
  
  if error == "":
    return render(request, 'add-product.html', {
      'categories': categories,
      'form': form
    })
    
  return render(request, 'add-product.html', {
    'categories': categories,
    'error': error,
      'form': form
  })


def edit_product(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')

  if request.method == "GET":
    return show_edit_product_page(request)
  
  id = request.POST.get('id')
  name = request.POST.get('name')
  price = request.POST.get('price')
  category_id = request.POST.get('category')

  product = Product.objects.filter(id=id).first()
  if product is None:
    return redirect('list-products')
  
  if name is None or name == "" or price is None or float(price) < 1:
    return show_edit_product_page(request, error='Invalid values')

  category = Category.objects.filter(id=category_id).first()
  if category is None:
    return show_edit_product_page(request, error='Category doesn\'t exist')

  product.name = name
  product.price = price
  product.category = category
  product.save()
  
  return redirect('list-products')


def show_edit_product_page(request: HttpRequest, error: str = ""):
  id = request.GET.get('id')
  if id is None or id == "":
    return redirect('list-products')
  
  product = Product.objects.filter(id=id).first()
  if product is None:
    return redirect('list-products')
    
  categories = Category.objects.all()

  if error == "":
    return render(request, 'edit-product.html', {
      'product': product,
      'categories': categories
    })
    
  return render(request, 'edit-product.html', {
    'product': product,
    'categories': categories,
    'error': error
  })


def delete_product(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')

  id = request.GET.get('id')
  if id is None or id == "":
    return redirect('list-products')
  
  product = Product.objects.filter(id=id).first()
  if product is None:
    return redirect('list-products')

  product.delete()
  return redirect('list-products')
