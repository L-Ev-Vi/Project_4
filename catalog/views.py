from typing import Any

from django.http import HttpRequest
from django.shortcuts import render

from catalog.models import Product, Contacts


def index(request: HttpRequest) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта."""

    # получение списка продуктов из БД
    context = {"products": Product.objects.all()}
    # генерация HTML-кода при GET-запросе (главной страницы каталога)
    return render(request, "catalog/index.html", context)


def contacts(request: HttpRequest) -> Any:
    """Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами."""

    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
        return render(request, "catalog/message.html", {"name": name})
    # вывод данных из БД таблицы 'contacts' для отображения на странице 'Контакты'
    context = {"contact": Contacts.objects.get()}
    # генерация HTML-кода при GET-запросе (страницы Контактов)
    return render(request, "catalog/contacts.html", context)


def product_item(request: HttpRequest, product_id: int) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление страницу с продуктом."""

    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
        return render(request, "catalog/message.html", {"name": name})
    # получение объекта-продукт из БД по уникальному идентификатору
    context = {"product": Product.objects.get(id=product_id)}
    # генерация HTML-кода при GET-запросе (главной страницы каталога)
    return render(request, "catalog/product_item.html", context)
