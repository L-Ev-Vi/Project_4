from django import forms
from blog.models import Article
from typing import Any

class ArticleForm(forms.ModelForm):
    """Класс представляющий форму для добавления и редактирования статьи."""

    class Meta:
        """Клас для добавления данных к форме."""
        model = Article
        fields = ["heading", "content", "image", "publication"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Метод стилизации полей формы."""
        super().__init__(*args, **kwargs)
        self.fields["heading"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Заголовок статьи'})
        self.fields["content"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст'})
        self.fields["image"].widget.attrs.update({'class': 'form-control'})
        self.fields["publication"].widget.attrs.update({'class': 'form-check-input'})