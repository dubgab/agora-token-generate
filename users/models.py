"""User Model"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User models.
        Extends from django's abstrac user, change the username fields to
        email and add some extra fields.
    """
    email = models.EmailField(
        'Correo Electrónico',
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist'
        }
    )
    name = models.CharField("Nombre", max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    is_superuser = models.BooleanField("Superusuario", default=False)

    def __str__(self):
        """Return username and email"""
        return f'{self.name} - {self.email}'

    def get_short_name(self):
        """Return username"""
        return self.name
