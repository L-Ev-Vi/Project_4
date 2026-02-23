from django.shortcuts import render, get_object_or_404
from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Article


class ListArticles(ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу со статьями блога, начиная с последней опубликованной статьи."""

    model = Article  # определяем модель
    template_name = "blog/blog.html"  # определяем шаблон
    context_object_name = "blogs"  # определяем переменную для использования в шаблоне


class CreateArticles(CreateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для добавления статьи."""

    model = Article  # определяем модель
    fields = ["heading", "content", "image", "publication"]  # указываем поля формы
    template_name = "blog/add_article.html"  # определяем шаблон
    success_url = reverse_lazy("blog:blog")  # определяем URL-адрес для перехода


class DetailArticle(DetailView):
    """Классовое представление принимающее GET запрос и возвращающее страницу статьи."""

    model = Article  # определяем модель
    template_name = "blog/article.html"  # определяем шаблон
    context_object_name = "article"  # определяем переменную для использования в шаблоне


class UpdateArticles(UpdateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу редактирования статьи."""

    model = Article  # определяем модель
    fields = ["heading", "content", "image", "publication"]  # указываем поля формы
    template_name = "blog/update_article.html"  # определяем шаблон
    success_url = reverse_lazy("blog:blog")  # определяем URL-адрес для перехода


class DeleteArticle(DeleteView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу подтверждения об удалении статьи."""

    model = Article  # определяем модель
    template_name = "blog/delete_article.html"  # определяем шаблон
    success_url = reverse_lazy("blog:blog")  # определяем URL-адрес для перехода
    context_object_name = "article"  # определяем переменную для использования в шаблоне