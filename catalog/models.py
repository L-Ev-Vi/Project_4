from django.conf import settings
from django.db import models


class Category(models.Model):
    """Класс описывающий структуру таблицы с категориями товаров."""

    name = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self) -> str:
        """Метод определяет строковое представление объекта."""
        return f"{self.name}"

    class Meta:
        """Клас который добавляет метаданные к модели Category."""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        db_table = "category"


class Product(models.Model):
    """Класс описывающий структуру таблицы с товарами."""

    name: str = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="images/", default="images/default.jpg", blank=True, verbose_name="Изображения"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product", verbose_name="категория")
    price = models.FloatField(verbose_name="Цена")
    publication = models.BooleanField(default=False, verbose_name="Признак публикации")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Пользователь",
    )

    def __str__(self) -> str:
        """Метод определяет строковое представление объекта."""
        return f"{self.name} - {self.price}"

    def delete(self, *args, **kwargs):
        """При вызове метода 'delete' медиафайл также автоматически удаляется bpb cbcntvs."""
        self.image.delete()
        super(Product, self).delete(*args, **kwargs)

    class Meta:
        """Клас который добавляет метаданные к модели Category."""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        db_table = "product"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Contacts(models.Model):
    """Класс описывающий структуру таблицы для хранения контактных данных."""

    address = models.CharField(max_length=250, verbose_name="Адрес")
    country = models.CharField(max_length=50, verbose_name="Страна")
    inn = models.IntegerField(verbose_name="ИНН")
    phone = models.CharField(max_length=12, verbose_name="Контактный телефон")

    def __str__(self) -> str:
        """Метод определяет строковое представление объекта."""
        return f"{self.address} - {self.phone}"

    class Meta:
        """Клас который добавляет метаданные к модели Category."""

        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["phone"]
        db_table = "contacts"


# class Appeals(models.Model):
#     """Класс описывающий структуру таблицы для хранения контактных данных при обращении пользователей."""
#
#     name = models.CharField(max_length=80, verbose_name="Имя")
#     phone = models.CharField(max_length=12, verbose_name="Контактный телефон")
#     email = models.EmailField(max_length = 254, verbose_name="Электронная почта")
#     message = models.TextField(blank=True, null=True, verbose_name="Сообщение")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время обращения")
#
#     def __str__(self) -> str:
#         """Метод определяет строковое представление объекта."""
#         return f"{self.name} - {self.phone}"
#
#     class Meta:
#         """Клас который добавляет метаданные к модели Category."""
#
#         verbose_name = "Обращение"
#         verbose_name_plural = "Обращения"
#         ordering = ["name", "phone", "email"]
#         db_table = "appeals"
