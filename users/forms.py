from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from users.models import User


class MixinStyle:
    """Класс-миксин задающий стиль для формы."""

    def __init__(self, *args, **kwargs):
        """Метод стилизации полей формы."""
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            if isinstance(value, bool):
                self.fields[key].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[key].widget.attrs.update({'class': 'form-control'})


class FormUser(MixinStyle, UserCreationForm):
    """Класс представляющий форму для регистрации пользователей."""
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "username", "first_name", "last_name", "country", "phone_number", "avatar"]


class AuthenticationUser(MixinStyle, AuthenticationForm):
    """Класс представляющий форму для входа пользователя в систему."""
    pass


class ChangeUser(UserChangeForm):
    """Класс представляющий форму для редактирования пользователей."""

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["email", "username", "first_name", "last_name", "country", "phone_number", "avatar", "password",]

    def __init__(self, *args, **kwargs) -> None:
        """Метод стилизации полей формы."""
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control", "aria-label": "Выберите категорию"})
        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Название товара"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder": "Описание"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder": "Цена товара"})
        self.fields["country"].widget.attrs.update({"class": "form-select", "placeholder": "Цена товара"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control", "placeholder": "Цена товара"})
        self.fields["avatar"].widget.attrs.update({"class": "form-control", "accept": "/media/*"})


class PasswordChangeUserForms(MixinStyle, PasswordChangeForm):
    """Класс представляющий форму для смены пароля пользователя."""
    pass
