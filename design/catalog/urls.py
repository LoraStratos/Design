from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', ApplicationViewIndex.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('application/', ApplicationViewUser.as_view(), name='my_application'),
    path('validate_username', validate_username, name='validate_username'),
    path('profile/', profile, name='profile'),
    path('create_application/', ApplicationCreate.as_view(), name='create_ap'),
    path('application/<pk>/delete/', ApplicationDelete.as_view(), name='delete_ap'),

    path('category/', CategoryView.as_view(), name='category'),
    path('all_application/', ApplicationViewAdmin.as_view(), name='all_application'),
    path('change/<pk>/status/', ChangeStatus.as_view(), name='change_status'),
    path('create_category/', CategoryCreate.as_view(), name='create_category'),
    path('category/<pk>/delete/', CategoryDelete.as_view(), name='delete_category'),
]

