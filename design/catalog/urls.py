from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('profile/', views.profile, name='profile'),
]