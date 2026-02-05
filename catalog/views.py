from pydoc import HTMLDoc

from django.shortcuts import render


def index(request) -> HTMLDoc:
    """Контроллер принимающий GET запрос и возвращающий ответом представление главной страницы проекта."""
    return render(request, "catalog/index.html")


def contacts(request) -> HTMLDoc:
    """Контроллер принимающий GET и POST запросы, и возвращающий ответом представление страницы с контактами."""
    if request.method == "POST":
        name = request.POST.get("name")
        return render(request, "catalog/message.html", {"name": name})
    return render(request, "catalog/contacts.html")
