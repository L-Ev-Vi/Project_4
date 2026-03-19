from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Класс определяющий модель пользователя"""

    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Изображение")
    country = CountryField(blank_label="(Выберите страну)", blank=True, null=True, verbose_name="Страна")
    token = models.CharField(max_length=100, verbose_name="Токин", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        """Клас который добавляет метаданные к модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]
        db_table = "users"
