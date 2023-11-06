from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration/registration.html')

def profile(request):
    return render(request, 'profile.html')

class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')