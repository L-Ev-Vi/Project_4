import secrets
from typing import Any

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from catalog.models import Category
from catalog.views import MixinContextCreate
from users.forms import AuthenticationUser, ChangeUser, FormUser, PasswordChangeUserForms
from users.models import User


class MyLogin(LoginView):
    """Классовое представление для авторизации пользователей."""

    form_class = AuthenticationUser  # указываем форму
    template_name = "users/login_user.html"  # определяем шаблон

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class MyLogout(LogoutView):
    """Классовое представление для выхода пользователей из системы."""

    pass


class Verification(TemplateView):
    """Классовое представление принимающее GET запрос,
    и возвращающее страницу с сообщением об необходимости подтверждения почты."""

    template_name = "users/verification.html"  # определяем шаблон

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CreateUser(MixinContextCreate, CreateView):
    """Классовое представление для регистрации пользователей."""

    model = User  # определяем модель
    form_class = FormUser  # указываем форму
    template_name = "users/register_user.html"  # определяем шаблон
    success_url = reverse_lazy("users:verification")  # определяем URL-адрес для перехода

    def form_valid(self, form):
        """Метод отправки приветственного письма после успешной валидации формы."""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        self.send_welcome_email(user.email, url)
        return super().form_valid(form)

    def send_welcome_email(self, user_email, url):
        """Метод отправки приветственного письма на адрес электронной почты."""
        subject = "Добро пожаловать на наш сервис!"
        message = f"Для продолжения регистрации подтвердите почту по ссылке - {url}"
        recipient_list = [user_email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)


def email_verification(request, token):
    """Функция верификации пользователя по 'email'."""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    login(request, user)
    return redirect(reverse("catalog:catalog"))


class UpdateUser(MixinContextCreate, UpdateView):
    """Классовое представление для редактирования пользователя."""

    model = User  # определяем модель
    form_class = ChangeUser  # указываем форму
    template_name = "users/register_user.html"  # определяем шаблон
    success_url = reverse_lazy("catalog:catalog")  # определяем URL-адрес для перехода

    def get_object(self, queryset=None):
        return self.request.user


class PasswordsChangeUser(PasswordChangeView):
    """Классовое представление для смены пароля пользователя."""

    model = User  # определяем модель
    form_class = PasswordChangeUserForms  # указываем форму
    template_name = "users/change-password.html"  # определяем шаблон
    success_url = reverse_lazy("users:edit_profile")  # определяем URL-адрес для перехода

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        """Метод отправки письма после успешного изменения пароля."""
        user = form.save()
        user.save()
        self.send_email(user.email)
        return super().form_valid(form)

    def send_email(self, user_email):
        """Метод отправки приветственного письма на адрес электронной почты."""
        subject = "Уведомление о смене пароля!"
        message = "Ваш пароль был успешно изменён!"
        recipient_list = [user_email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
