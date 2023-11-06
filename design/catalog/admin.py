from django.contrib import admin
from .models import CustomUser, Category, Application

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Application)