from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление категорий и продуктов тестирования в базу данных"

    def handle(self, *args, **options) -> None:
        """Метод добавления данных в БД"""

        # Product.objects.all().delete()  # предварительное удаление данных из таблицы Product перед загрузкой новых
        Category.objects.all().delete()  # предварительное удаление данных из таблицы Category перед загрузкой новых

        with connection.cursor() as cur:
            cur.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        categories = [{"name": "Костюмы мягкие мужские", "description": "Удобные тёплые"},
                      {"name": "Костюмы обтягивающие мужские", "description": "Не натирают"},
                      {"name": "Костюмы обтягивающие женские",
                       "description": "Неудобно, но что поделать, зато красиво."},
                      {"name": "Женские штучки", "description": "Отличный подарок на 14 февраля."}, ]

        for category_data in categories:
            Category.objects.create(**category_data)

        # call_command("loaddata", "catalog/product_fixture.json", "--ignorenonexistent")
