from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(
        max_length=20,
        help_text=_('Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.'),
    )
    password = models.CharField(
        max_length=100,
        help_text=_('Your password must contain at least 3 characters.'),
    )
    password_confirmation = models.CharField(
        max_length=100,
        help_text=_('To confirm, please enter the password again.'),
    )

    def __str__(self):
        return self.username
