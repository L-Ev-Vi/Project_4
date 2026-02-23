from django.contrib import admin

from blog.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Класс регистрации и настройки отображения модели 'Article' в админке"""

    list_display = (
        "pk",
        "heading",
        "publication",
        "created_at",
        "number_views",
    )
    list_filter = ("publication",)
    search_fields = (
        "name",
        "content",
    )
