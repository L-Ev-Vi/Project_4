from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", 'полиция', "радар"]


class ProductForm(forms.ModelForm):
    """Класс представляющий форму для добавления и редактирования продуктов."""

    class Meta:
        """Клас для добавления данных к форме."""
        model = Product  # определяем модель
        fields = ["category", "name", "description", "price", "image", "publication"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Метод стилизации полей формы."""
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({'class': 'form-select', 'aria-label': 'Выберите категорию'})
        self.fields["name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название товара'})
        self.fields["description"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Описание'})
        self.fields["price"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена товара'})
        self.fields["image"].widget.attrs.update({'class': 'form-control', 'accept': '/media/*'})
        self.fields["publication"].widget.attrs.update({'class': 'form-check-input'})

    def clean_name(self) -> Any:
        """Метод валидации названия товара."""
        name = self.cleaned_data.get("name")
        names = name.split()
        for word in names:
            if word.lower() in FORBIDDEN_WORDS:
                raise ValidationError(f"Названии товара содержит не допустимое слово '{word}'!")
        return name

    def clean_description(self) -> Any:
        """Метод валидации описания товара."""
        description = self.cleaned_data.get("description")
        words = description.split()
        for word in words:
            if word.lower() in FORBIDDEN_WORDS:
                raise ValidationError(f"В описании товара содержится не допустимое слово '{word}'!")
        return description

    def clean_price(self) -> Any:
        """Метод валидации цены товара. Метод исключает отрицательное значение цены"""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной!")
        return price
