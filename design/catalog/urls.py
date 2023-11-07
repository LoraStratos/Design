from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('profile/', views.ApplicationView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

