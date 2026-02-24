import os
from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dotenv import load_dotenv

from blog.models import Article
from blog.utils import send_email_tu_user

load_dotenv(verbose=True)


class ListArticles(ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу со статьями блога,
    начиная с последней опубликованной статьи."""

    model = Article  # определяем модель
    template_name = "blog/blog.html"  # определяем шаблон
    context_object_name = "blogs"  # определяем переменную для использования в шаблоне

    def get_queryset(self) -> Any:
        """Переопределённый метод 'get_queryset'.
        Метод отбирает только те статьи у которых метод публикации равин 'True'."""

        return super().get_queryset().filter(publication=True)


class CreateArticles(CreateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для добавления статьи."""

    model = Article  # определяем модель
    fields = ["heading", "content", "image", "publication"]  # указываем поля формы
    template_name = "blog/add_article.html"  # определяем шаблон
    success_url = reverse_lazy("blogs:blogs")  # определяем URL-адрес для перехода


class DetailArticle(DetailView):
    """Классовое представление принимающее GET запрос и возвращающее страницу статьи."""

    model = Article  # определяем модель
    template_name = "blog/article.html"  # определяем шаблон
    context_object_name = "article"  # определяем переменную для использования в шаблоне

    def get_object(self, queryset=None) -> Any:
        """Метод используется для получения одного объекта, который будет отображаться в представлении.
        Метод увеличивает значение поля просмотров на одну единицу при каждом переходе на конкретный объект (статью)."""

        obj = super().get_object(queryset)
        obj.number_views += 1
        obj.save()
        # логика отправки сообщения на указанный адрес электронной почты при достижении 100 просмотров статьи
        if obj.number_views == 100:
            mail = os.getenv("EMAIL_USER")
            send_email_tu_user(mail, "Уведомление",
                               f"Количество просмотров поста {obj.heading}, достигло 100 просмотров!")
        return obj


class UpdateArticles(UpdateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу редактирования статьи."""

    model = Article  # определяем модель
    fields = ["heading", "content", "image", "publication"]  # указываем поля формы
    template_name = "blog/add_article.html"  # определяем шаблон

    def get_success_url(self) -> None:
        """Метод перенаправления на страницу статьи после её редактирования."""

        return reverse_lazy("blogs:article", kwargs={"pk": self.object.pk})


class DeleteArticle(DeleteView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу подтверждения об удалении статьи."""

    model = Article  # определяем модель
    template_name = "blog/delete_article.html"  # определяем шаблон
    success_url = reverse_lazy("blogs:blogs")  # определяем URL-адрес для перехода
    context_object_name = "article"  # определяем переменную для использования в шаблоне
