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
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Изображения")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product", verbose_name="категория")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self) -> str:
        """Метод определяет строковое представление объекта."""
        return f"{self.name} - {self.price}"

    class Meta:
        """Клас который добавляет метаданные к модели Category."""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        db_table = "product"
