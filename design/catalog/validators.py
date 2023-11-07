from django.core.exceptions import ValidationError

def validate_password_len(password):
    if len(password) < 8:
        raise ValidationError('Длина пароля не должна быть меньше 8 символов')