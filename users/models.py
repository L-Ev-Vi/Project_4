from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class User(AbstractUser):
    """Класс определяющий модель пользователя"""

    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Изображение")
    country = CountryField(blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email