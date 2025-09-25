from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def login(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'login.html')

    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email != "admin@gmail.com" or password != "Admin@1234":
        return HttpResponse("Wrong email or password")
    
    return HttpResponse("Logged in")

def signup(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'signup.html')

    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm-password')
    
    if password != confirmPassword:
        return HttpResponse("Passwords do not match")

    # Validate email format
    # Validate password format
    
    # Same email check
    
    return HttpResponse("Signed up")