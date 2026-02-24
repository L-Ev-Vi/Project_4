from django.db import models

class Article(models.Model):
    """Класс описывающий структуру таблицы с товарами."""

    heading = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Изображение")
    publication = models.BooleanField(default=True, verbose_name="Признак публикации")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    number_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self) -> str:
        """Метод определяет строковое представление объекта."""
        return f"{self.heading} - {self.created_at}"

    class Meta:
        """Клас который добавляет метаданные к модели Category."""

        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]
        db_table = "article"
