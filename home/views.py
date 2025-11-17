from django.http import HttpRequest
from django.shortcuts import render, redirect


def home(request: HttpRequest):
  if request.COOKIES.get('email') is None:
    return redirect('login')
  
  return render(request, 'home.html')
