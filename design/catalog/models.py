from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name='Имя', unique=True, blank=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', unique=True, blank=False)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.EmailField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Введите краткое описание заявки")
    category = models.ForeignKey(Category, help_text="Выберите категорию заявки", on_delete=models.CASCADE, default='0')

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    photo_file = models.ImageField(max_length=254, upload_to='image/', validators=[validate_image, FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(verbose_name='Дата добавления')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('application_list', args=[str(self.id)])

    def __str__(self):
        return self.title