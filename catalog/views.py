from typing import Any

from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> Any:
    """Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта."""
    return render(request, "catalog/index.html")


def contacts(request: HttpRequest) -> Any:
    """Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами."""
    if request.method == "POST":
        name = request.POST.get("name")
        # генерация HTML-кода при POST-запросе(заполнение и отправка формы)
        return render(request, "catalog/message.html", {"name": name})
    # генерация HTML-кода при GET-запросе
    return render(request, "catalog/contacts.html")
