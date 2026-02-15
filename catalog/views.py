from typing import Any

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404

from catalog.models import Product, Contacts, Category


def index(request: HttpRequest) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта."""

    # получение списка продуктов из БД
    context = {"products": get_list_or_404(Product)}
    # генерация HTML-кода при GET-запросе (главной страницы каталога)
    return render(request, "catalog/index.html", context)


def contacts(request: HttpRequest) -> Any:
    """Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами."""

    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
        return render(request, "catalog/message.html", {"name": name})
    # вывод данных из БД таблицы 'contacts' для отображения на странице 'Контакты'
    context = {"contact": get_object_or_404(Contacts)}
    # генерация HTML-кода при GET-запросе (страницы Контактов)
    return render(request, "catalog/contacts.html", context)


def product_item(request: HttpRequest, product_id: int) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление страницу с продуктом."""

    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
        return render(request, "catalog/message.html", {"name": name})
    # получение объекта-продукт из БД по уникальному идентификатору
    context = {"product": get_object_or_404(Product, id=product_id)}
    # генерация HTML-кода при GET-запросе (страницы продукта)
    return render(request, "catalog/product_item.html", context)


def add_product(request: HttpRequest) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление страницы для добавления продукта."""

    if request.method == "POST":
        # создание объекта-продукт и добавление его в БД
        category_id = int(request.POST.get("category"))
        Product.objects.create(name=request.POST.get("name"), description=request.POST.get("description"),
                               category=Category.objects.get(id=category_id), price=request.POST.get("price"),
                               image=request.POST.get("image"))
        # генерация HTML-кода при POST-запросе(при заполнении данных о продукте и отправке формы)
        return render(request, "catalog/product_added.html")
    # получение списка продуктов из БД
    context = {"categories": get_list_or_404(Category)}
    # генерация HTML-кода при GET-запросе (главной страницы каталога)
    return render(request, "catalog/add_product.html", context)
