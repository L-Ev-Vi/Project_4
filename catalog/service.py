from django.conf import settings
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .models import Category, Contacts, Product


class CatalogService:
    """Класс описывающий методы бизнес-логики приложения 'catalog'."""

    @staticmethod
    def get_list_categories():
        """Метод передаёт список категорий."""
        if settings.CACHE_ENABLED:
            key = "categories"
            categories = cache.get(key)
            if not categories:
                categories = Category.objects.all()
                cache.set(key, categories, 60 * 60)
            return categories
        return Category.objects.all()

    @staticmethod
    def get_category(category_id):
        """Метод передаёт категорию."""
        if settings.CACHE_ENABLED:
            key = f"category_{category_id}"
            category = cache.get(key)
            if not category:
                category = Category.objects.get(id=category_id)
                cache.set(key, category, 60 * 60)
            return category
        return Category.objects.get(id=category_id)

    @staticmethod
    def get_list_products():
        """Метод передаёт список продуктов."""
        if settings.CACHE_ENABLED:
            key = "products"
            products = cache.get(key)
            if not products:
                products = Product.objects.filter(publication=True)
                cache.set(key, products, 60 * 15)
            return products
        return Product.objects.filter(publication=True)

    @staticmethod
    def get_list_products_category(category_id):
        """Метод передаёт список продуктов в указанной категории."""
        if settings.CACHE_ENABLED:
            key = f"products_{category_id}"
            products = cache.get(key)
            if not products:
                products = Product.objects.filter(publication=True, category=category_id)
                cache.set(key, products, 60 * 15)
            return products
        return Product.objects.filter(publication=True, category=category_id)

    @staticmethod
    def get_contacts():
        """Метод передаёт контакты."""
        if settings.CACHE_ENABLED:
            key = "contacts"
            contacts = cache.get(key)
            if not contacts:
                contacts = get_object_or_404(Contacts)
                cache.set(key, contacts, 60 * 10080)
            return contacts
        return get_object_or_404(Contacts)
