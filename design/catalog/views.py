from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

def registration(request):
    return render(request, 'registration/registration.html')