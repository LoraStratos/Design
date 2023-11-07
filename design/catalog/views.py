from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Application


def index(request):
    return render(request, 'index.html')

def logout(request):
    return render(request, 'registration/logout.html')


def profile(request):
    return render(request, 'profile.html')

class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def registration(request):
        return render(request, 'registration/registration.html')

def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

class ApplicationView(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'profile.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

