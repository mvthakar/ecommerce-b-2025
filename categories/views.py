from django.http import HttpRequest
from django.shortcuts import redirect, render
from .models import Category


def show_category_list_page(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  categories = Category.objects.all()
  
  return render(request, 'list.html', {
    'categories': categories
  })


def add_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')

  if request.method == "GET":
    return show_add_category_page(request)
  
  name = request.POST.get('name')
  if name is None or name == "":
    return show_add_category_page(request, "Name cannot be empty")
  
  Category.objects.create(name=name)
  return redirect('list-categories')


def show_add_category_page(request: HttpRequest, error: str = ""):
  if error == "":
    return render(request, 'add.html')
  
  return render(request, 'add.html', {
    'error': error
  })


def edit_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')

  if request.method == "GET":
    return show_edit_category_page(request)

  id = request.POST.get('id')
  name = request.POST.get('name')
  
  if id is None or id == "" or name is None or name == "":
    return show_edit_category_page(request, error="Empty values not allowed")
  
  category = Category.objects.filter(id=id).first()
  if category is None:
    return redirect('list-categories')

  category.name = name
  category.save()

  return redirect('list-categories')


def show_edit_category_page(request: HttpRequest, error: str = ""):
  id = request.GET.get("id")
  if id is None or id == "":
    return redirect('list-categories')
  
  category = Category.objects.filter(id=id).first()
  if category is None:
    return redirect('list-categories')

  if error == "":
    return render(request, 'edit.html', {
      'category': category      
    })
  
  return render(request, 'edit.html', {
    'error': error,
    'category': category
  })

def delete_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  id = request.GET.get('id')
  if id is None or id == "":
    return redirect('list-categories')
  
  category = Category.objects.filter(id=id).first()
  if category is None:
    return redirect('list-categories')
    
  category.delete()
  return redirect('list-categories')
