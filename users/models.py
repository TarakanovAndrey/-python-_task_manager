from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(
        max_length=150,
        help_text=_('Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.'),
        unique=True,

        # необходима функция валидотор для провреки наличия только цифры и символы @/./+/-/_.
    )
    password = models.CharField(
        max_length=100,
        help_text=_('Your password must contain at least 3 characters.'),
    )
    password_confirmation = models.CharField(
        max_length=100,
        help_text=_('To confirm, please enter the password again.'),
        validators=[MinLengthValidator(3, message='The password entered is too short. It must contain at least 3 characters.')],
    )

    def __str__(self):
        return self.username
