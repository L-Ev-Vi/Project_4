from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс регистрации и настройки отображения модели 'Category' в админке"""

    list_display = (
        "pk",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс регистрации и настройки отображения модели 'Product' в админке"""

    list_display = (
        "pk",
        "name",
        "price",
        "category",
        "created_at",
        "updated_at",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Класс регистрации и настройки отображения модели 'Contacts' в админке"""
    list_display = (
        "pk",
        "address",
        "country",
        "inn",
        "phone",
    )
    list_filter = ("country",)
