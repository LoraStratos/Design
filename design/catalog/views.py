from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import RegisterUserForm, ChangeStatusApplication
from .models import Application, Category


def profile(request):
    return render(request, 'profile.html')


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def registration(self):
        return render(self, 'registration/registration.html')

def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

class ApplicationViewUser(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'my_application.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user).order_by('-date')

class ApplicationViewIndex(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'index.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(status='C')

    def index(self):
        num_applications = Application.objects.filter(status='P').count()
        return render(self, 'index.html', context={'num_application': num_applications})


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['title', 'description', 'category', 'photo_file']
    template_name = 'create_application.html'
    success_url = reverse_lazy('my_application')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def create_application(self):
        return render(self, "create_application.html")

class ApplicationDelete(DeleteView):
    model = Application
    context_object_name = 'application'
    template_name = 'delete_application.html'
    success_url = reverse_lazy('my_application')

    def delete_application(self, pk):
        application = Application.objects.filter(user=self.request.user, pk=pk)
        if application:
            application.delete()
        return redirect('my_application')

class ApplicationViewAdmin(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'admin/all_application.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.order_by('-date')

class CategoryView(generic.ListView):
    model = Category
    template_name = 'admin/category.html'
    context_object_name = 'category'

class ChangeStatus(UpdateView):
    model = Application
    form_class = ChangeStatusApplication
    template_name = 'admin/change_status.html'
    success_url = reverse_lazy('all_application')

    def change_status(self):
        return render(self, 'admin/change_status.html')

class CategoryDelete(DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'admin/delete_category.html'
    success_url = reverse_lazy('category')

    def category(self, pk):
        category = Category.objects.filter(pk=pk)
        if category:
            category.delete()
        return redirect('category')

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'admin/create_category.html'
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def create_application(self):
        return render(self, "admin/create_category.html")
