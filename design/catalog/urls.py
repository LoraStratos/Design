from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', ApplicationViewIndex.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('application/', my_application, name='my_application'),
    path('validate_username', validate_username, name='validate_username'),
    path('profile/', ApplicationViewUser.as_view(), name='profile'),
]

