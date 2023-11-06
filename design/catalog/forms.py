from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms

class RegisterUserForm(forms.ModelForm):
    full_name = forms.CharField(
        label='ФИО',
        validators=[RegexValidator('^[а-яА-Я- -]+$',
        message="Разрешены только кириллица, дефис и пробелы")],
        error_messages={'required': 'Обязательное поле',}
    )

