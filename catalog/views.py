from typing import Any

from django.http import HttpRequest
from django.shortcuts import render

from catalog.models import Product, Contacts


def index(request: HttpRequest) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта."""

    # отображение последних 5 созданных продуктов в консоли
    five_products = Product.objects.all()
    for i in range(5):
        if i < 5:
            print(five_products[len(five_products) - (5 - i)])
    # генерация HTML-кода при GET-запросе (главной страницы каталога)
    return render(request, "catalog/index.html")


def contacts(request: HttpRequest) -> Any:
    """Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами."""

    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
        return render(request, "catalog/message.html", {"name": name})
    # вывод данных из БД таблицы 'contacts' для отображения на странице 'Контакты'
    contact = Contacts.objects.all()
    context = {"address": contact[0].address,
               "country": contact[0].country,
               "inn": contact[0].inn,
               "phone": contact[0].phone}
    # генерация HTML-кода при GET-запросе (страницы Контактов)
    return render(request, "catalog/contacts.html", context)
