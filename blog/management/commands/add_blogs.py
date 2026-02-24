from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from blog.models import Article


class Command(BaseCommand):
    help = "Добавление постов для тестирования в базу данных"

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Метод добавления данных в БД"""

        Article.objects.all().delete()  # предварительное удаление данных из таблицы article перед загрузкой новых

        # сброс инкремента (счётчика 'id' до 1)
        with connection.cursor() as cur:
            cur.execute("ALTER SEQUENCE article_id_seq RESTART WITH 1")  # чистый SQL запрос

        call_command("loaddata", "blog/article_fixture.json", "--ignorenonexistent")
