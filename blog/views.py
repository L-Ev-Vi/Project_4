from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.forms import ArticleForm
from blog.models import Article
from blog.utils import send_email_tu_user


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


class CreateArticles(LoginRequiredMixin, CreateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для добавления статьи."""

    model = Article  # определяем модель
    form_class = ArticleForm  # указываем форму
    template_name = "blog/add_article.html"  # определяем шаблон
    success_url = reverse_lazy("blogs:blogs")  # определяем URL-адрес для перехода

    def form_valid(self, form):
        """Метод определения автора статьи после успешной валидации формы."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DetailArticle(DetailView):
    """Классовое представление принимающее GET запрос и возвращающее страницу статьи."""

    model = Article  # определяем модель
    template_name = "blog/article.html"  # определяем шаблон
    context_object_name = "article"  # определяем переменную для использования в шаблоне

    def get_object(self, queryset: Any = None) -> Any:
        """Метод используется для получения одного объекта, который будет отображаться в представлении.
        Метод увеличивает значение поля просмотров на одну единицу при каждом переходе на конкретный объект (статью).
        """

        obj = super().get_object(queryset)
        obj.number_views += 1
        obj.save()
        # логика отправки сообщения на указанный адрес электронной почты при достижении 100 просмотров статьи
        if obj.number_views == 100:
            mail = obj.owner.email
            send_email_tu_user(
                mail, "Уведомление", f"Количество просмотров поста '{obj.heading}', достигло 100 просмотров!"
            )
        return obj


class UpdateArticles(LoginRequiredMixin, UpdateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу редактирования статьи."""

    model = Article  # определяем модель
    form_class = ArticleForm  # указываем форму
    template_name = "blog/add_article.html"  # определяем шаблон

    def get_success_url(self) -> str:
        """Метод перенаправления на страницу статьи после её редактирования."""
        return reverse_lazy("blogs:article", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        """Метод выполняющий проверку прав доступа на редактирование статьи."""
        user = self.request.user
        if user == self.object.owner:
            return ArticleForm
        elif user.has_perm("blog.change_article"):
            return ArticleForm
        else:
            raise PermissionDenied


class DeleteArticle(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Классовое представление принимающее GET и POST запросы,
    и возвращающее страницу подтверждения об удалении статьи."""

    model = Article  # определяем модель
    template_name = "blog/delete_article.html"  # определяем шаблон
    success_url = reverse_lazy("blogs:blogs")  # определяем URL-адрес для перехода
    context_object_name = "article"  # определяем переменную для использования в шаблоне

    def test_func(self):
        """Метод проверки условия на доступ к представлению."""
        return self.request.user.has_perm("blog.delete_article") or self.get_object().owner == self.request.user
