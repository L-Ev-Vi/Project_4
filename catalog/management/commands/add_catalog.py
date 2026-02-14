from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection
from typing import Any

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление категорий и продуктов тестирования в базу данных"

    def handle(self, *args: Any, **options: Any) -> None:
        """Метод добавления данных в БД"""

        Product.objects.all().delete()  # предварительное удаление данных из таблицы product перед загрузкой новых
        Category.objects.all().delete()  # предварительное удаление данных из таблицы category перед загрузкой новых

        # сброс инкремента (счётчика 'id' до 1)
        with connection.cursor() as cur:
            cur.execute("ALTER SEQUENCE category_id_seq RESTART WITH 1")  # чистый SQL запрос
        with connection.cursor() as cur:
            cur.execute("ALTER SEQUENCE product_id_seq RESTART WITH 1")  # чистый SQL запрос
        # данные операции были выполнены в рамках тестирования и не рекомендуются для массового использования

        categories = [
            {"name": "Костюмы мягкие мужские", "description": "Удобные тёплые"},
            {"name": "Костюмы обтягивающие мужские", "description": "Не натирают"},
            {"name": "Костюмы обтягивающие женские", "description": "Неудобно, но что поделать, зато красиво."},
            {"name": "Женские штучки", "description": "Отличный подарок на 14 февраля."},
        ]

        for category_data in categories:
            Category.objects.create(**category_data)

        call_command("loaddata", "catalog/product_fixture.json", "--ignorenonexistent")
