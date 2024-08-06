from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="email",
        help_text="укажите ваш email",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        help_text="укажите ваш телефон",
        **NULLABLE,
    )
    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        **NULLABLE,
    )
    chat_id = models.CharField(
        max_length=255,
        verbose_name="chat_id",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email}"
