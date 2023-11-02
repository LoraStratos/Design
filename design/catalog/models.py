from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Application(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="Опишите свою заявку")

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Введите категорию")
    def __str__(self):
        return self.name
