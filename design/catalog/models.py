from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп.',
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Особые разрешения для этого пользователя.',
        related_name="customuser_set",
        related_query_name="user",
    )
    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])

class Application(models.Model):
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Введите краткое описание заявки")
    category = models.ManyToManyField(Category, help_text="Выберите категорию заявки")
    photo_file = models.ImageField(max_length=254, upload_to='image/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(verbose_name='Дата добавления')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
