from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

# from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ModeratorProductForm, ProductForm
from catalog.models import Category, Contacts, Product
from catalog.service import CatalogService


class MixinContextList(ListView):
    """Класс-миксин возвращающий ссылку на список товаров"""

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий."""
        context = super().get_context_data(**kwargs)
        context["categories"] = CatalogService.get_list_categories()
        return context


class MixinContextCreate(CreateView):
    """Класс-миксин возвращающий ссылку на один товаров"""

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий."""
        context = super().get_context_data(**kwargs)
        context["categories"] = CatalogService.get_list_categories()
        return context


# CBV


class CatalogView(MixinContextList, ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу с товарами."""

    model = Product  # определяем модель
    template_name = "catalog/index.html"  # определяем шаблон
    context_object_name = "page_object"  # определяем переменную для использования в шаблоне
    paginate_by = 6  # определяем количество продуктов на странице

    def get_queryset(self) -> Any:
        """Переопределённый метод 'get_queryset'.
        Метод отбирает только те товары у которых метод публикации равин 'True'."""
        return CatalogService.get_list_products()


class ProductCategoriesView(MixinContextList, ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу с товарами."""

    model = Product  # определяем модель
    template_name = "catalog/product_category.html"  # определяем шаблон
    context_object_name = "page_object"  # определяем переменную для использования в шаблоне
    paginate_by = 6  # определяем количество продуктов на странице

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["cate"] = CatalogService.get_category(self.kwargs["pk"])
        return context

    def get_queryset(self) -> Any:
        """Переопределённый метод 'get_queryset'.
        Метод отбирает только товары относящиеся к одной категории и у которых метод публикации равин 'True'."""
        return CatalogService.get_list_products_category(self.kwargs["pk"])


class ContactView(View):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу с контактами."""

    def get(self, request: HttpRequest) -> Any:
        """Метод генерации HTML-кода при GET-запросе (страницы Контактов)"""
        context = {"contact": CatalogService.get_contacts(), "categories": CatalogService.get_list_categories()}
        return render(request, "catalog/contacts.html", context)

    def post(self, request: HttpRequest) -> Any:
        """Метод генерации HTML-кода при POST-запросе(при заполнении и отправке формы).
        В методе передаются дополнительные данные об имени пользователя заполнившего форму"""
        name = request.POST.get("name")
        categories = CatalogService.get_list_categories()
        return render(request, "catalog/message.html", {"name": name, "categories": categories})


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductItemView(LoginRequiredMixin, DetailView):
    """Классовое представление принимающее GET запрос и возвращающее страницу описывающую свойства продукта."""

    model = Product  # определяем модель
    template_name = "catalog/product_item.html"  # определяем шаблон
    context_object_name = "product"  # определяем переменную для использования в шаблоне

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = CatalogService.get_list_categories()
        return context

    def post(self, request: HttpRequest, **kwargs: Any) -> Any:
        """Метод генерации HTML-кода при POST-запросе(при заполнении и отправке формы).
        В методе передаются дополнительные данные об имени пользователя заполнившего форму"""
        name = request.POST.get("name")
        categories = CatalogService.get_list_categories()
        return render(request, "catalog/message.html", {"name": name, "categories": categories})


class Message(TemplateView):
    """Классовое представление принимающее GET запрос,
    и возвращающее страницу с сообщением об успешном добавлении товара."""

    template_name = "catalog/product_added.html"  # определяем шаблон

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = CatalogService.get_list_categories()
        return context


class AddProductView(LoginRequiredMixin, MixinContextCreate, CreateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для добавления продукта.
    После успешного добавления продукта рендится страница об успешной операции."""

    model = Product  # определяем модель
    form_class = ProductForm  # указываем форму
    template_name = "catalog/add_product.html"  # определяем шаблон
    success_url = reverse_lazy("catalog:message")  # определяем URL-адрес для перехода

    def form_valid(self, form):
        """Метод определения пользователя, который добавил продукт, после успешной валидации формы."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateProductView(LoginRequiredMixin, MixinContextCreate, UpdateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для редактирования продукта.
    После успешного добавления продукта рендится страница продукта."""

    model = Product  # определяем модель
    form_class = ProductForm  # указываем форму
    template_name = "catalog/add_product.html"  # определяем шаблон

    def get_success_url(self) -> Any:
        """Метод перенаправления на страницу продукта после её редактирования."""
        return reverse_lazy("catalog:product_item", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        """Метод выполняющий проверку прав доступа на редактирование объекта."""
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm("catalog.can_unpublish_product"):
            return ModeratorProductForm
        else:
            raise PermissionDenied


class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Классовое представление принимающее GET и POST запросы,
    и возвращающее страницу подтверждения об удалении статьи."""

    model = Product  # определяем модель
    template_name = "catalog/delete_product.html"  # определяем шаблон
    success_url = reverse_lazy("catalog:catalog")  # определяем URL-адрес для перехода
    context_object_name = "product"  # определяем переменную для использования в шаблоне

    def get_context_data(self, **kwargs: Any) -> Any:
        """Переопределённый метод 'get_context_data'. Метод передаёт список категорий в шаблон."""
        context = super().get_context_data(**kwargs)
        context["categories"] = CatalogService.get_list_categories()
        return context

    def test_func(self):
        """Метод проверки условия на доступ к представлению."""
        return (
            self.request.user.has_perm("catalog.can_unpublish_product") or self.get_object().owner == self.request.user
        )


# FBV

# def index(request: HttpRequest) -> Any:
#     """Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта."""
#
#     # получение списка продуктов из БД
#     products = get_list_or_404(Product)
#     # создание списка пагинации для ограниченного количества продуктов на странице
#     paginator = Paginator(products, 6) # определяем количество продуктов на странице
#     page_number = request.GET.get("page")
#     page_object = paginator.get_page(page_number)
#     context = {"page_object": page_object}
#     # генерация HTML-кода при GET-запросе (главной страницы каталога)
#     return render(request, "catalog/index.html", context)


# def contacts(request: HttpRequest) -> Any:
#     """Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами."""
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
#         return render(request, "catalog/message.html", {"name": name})
#     # вывод данных из БД таблицы 'contacts' для отображения на странице 'Контакты'
#     context = {"contact": get_object_or_404(Contacts)}
#     # генерация HTML-кода при GET-запросе (страницы Контактов)
#     return render(request, "catalog/contacts.html", context)


# def product_item(request: HttpRequest, product_id: int) -> Any:
#     """Контроллер принимающий GET запрос и возвращающий представление страницу с продуктом."""
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         # генерация HTML-кода при POST-запросе(при заполнении и отправке формы)
#         return render(request, "catalog/message.html", {"name": name})
#     # получение объекта-продукт из БД по уникальному идентификатору
#     context = {"product": get_object_or_404(Product, id=product_id)}
#     # генерация HTML-кода при GET-запросе (страницы продукта)
#     return render(request, "catalog/product_item.html", context)


# def add_product(request: HttpRequest) -> Any:
#     """Контроллер принимающий GET запрос и возвращающий представление страницы для добавления продукта."""
#
#     if request.method == "POST":
#         # создание объекта-продукт и добавление его в БД
#         category_id = int(request.POST.get("category"))
#         Product.objects.create(name=request.POST.get("name"), description=request.POST.get("description"),
#                                category=Category.objects.get(id=category_id), price=request.POST.get("price"),
#                                image=request.POST.get("image"))
#         # генерация HTML-кода при POST-запросе(при заполнении данных о продукте и отправке формы)
#         return render(request, "catalog/product_added.html")
#     # получение списка продуктов из БД
#     context = {"categories": get_list_or_404(Category)}
#     # генерация HTML-кода при GET-запросе (главной страницы каталога)
#     return render(request, "catalog/add_product.html", context)
