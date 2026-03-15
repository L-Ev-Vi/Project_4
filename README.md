## Учебный проект Prodject_4
# *Проект создания интернет магазина, на базе фреймворка Django.*
*В проекте реализованны следующие задачи:*
+ *описана работа контролеров FBV и CBV;*
+ *настройка подключения к базе данных;*
+ *описаны модели;*
+ *выполнена регистрация моделей в админке;*
+ *маршрутизация;*
+ *шаблонизация;*
+ *настройка статики;*
+ *выполнение запросов через shel;*
+ *созданы фикстуры на основе созданных моделей;*
+ *описаны кастомные команды;*
+ *описана логика отправки электронной почты;*
+ *описана валидация и стилизация форм;*
+ *описана логика регистрации и авторизации пользователей;*

*Данные задачи были реализованны с использованием фреймворка Django который содержит весь не обходимый набора инструментов и библиотек
для создания веб-приложений. Данный проект предназначено для запуска с локального компьютера, способ запуска описан в разделе [установка](#установка) и [запуск проекта](#запуск-проекта).*

Более подробно о работе фреймворка Django можно узнать [здесь](https://djangodoc.ru/).

## *Содержание*
- [Цель проекта](#цель-проекта)
- [Инициализация Django в проект](#инициализация-Django-в-проект)
- [Первичные настройки](#первичные-настройки)
- [Создание и регистрация приложения](#создание-и-регистрация-приложения)
- [Создание контроллеров](#создание-контроллеров)
- [Настройка маршрутизации](#настройка-маршрутизации)
- [Создание моделей](#cоздание-моделей)
- [Миграции](#миграции)
- [Настройка админки](#настройка-админки)
- [Работа с Django shel](#работа-с-Django-shel)
- [Создание фикстур](#создание-фикстур)
- [Создание кастомных команд](#создание-кастомных-команд)
- [Создание шаблонов](#создание-шаблонов)
- [Настройка и добавление статики](#настройка-и-добавление-статики)
- [Создание и настройка форм](#создание-и-настройка-форм)
- [Установка](#установка)
- [Тестирование](#тестирование)
- [Запуск проекта](#запуск-проекта)
- [Команда проекта](#команда-проекта)

## Цель проекта
+ Закрепление теоретических навыков на практике;
+ Познакомится с фреймворком Django;
+ Изучить основные компоненты фреймворка Django;
+ Изучить структуру проекта Django и назначение основных файлов и директорий, таких как *manage.py, settings.py, urls.py и views.py;
+ Научится создавать и регистрировать приложения в Django;
+ Познакомиться с созданием контроллеров FBV и CBV (views) в Django, которые обрабатывают HTTP-запросы и формируют HTTP-ответы;
+ Узнать о механизмах маршрутизации в Django, связывающих URL-адреса с соответствующими контроллерами;
+ Изучить способы создания и подключения статических файлов (CSS, JS, изображения);
+ Вёрстка страниц с использованием HTML и CSS;
+ Познакомится с основными настройками для подключения БД в проекте Django;
+ Узнать, как создать и настроить модели в Django;
+ Рассмотреть основные методы работы с миграциями в Django;
+ Узнать, как создать и использовать фикстуры для предварительного наполнения БД данными;
+ Разобраться с созданием и использованием кастомных команд в Django;
+ Познакомится с настройками админки;
+ Освоить работу в Django shel;
+ Научится создавать и настраивать формы в Django;
+ Научится описывать логику регистрации пользователей в сервисе;
+ Разабратся с методами авторизации пользователей в Django;
+ Запуск локального-сервиса с использованием фреймворка Django;
+ Объединение и настройка всех компонентов в единое веб-приложение;

## Инициализация Django в проект
Для корректной работы проекта первым шагом было настроено виртуальное окружения `Poetry` для избежания конфликтов со сторонними библиотеками.

Затем с помощью команды `poetry add --group dev django` и `poetry add --group dev django-stubs` была выполнена установка *django* 
и *библиотечных заглушек*.

Для инициализации Django внутри директории проекта использовалась следующая команда:

`django-admin startproject config .`

После выполнения этой команды, в проекте создается директория *config*, внутри текущей директории создаются 
файлы конфигурации проекта.

## Первичные настройки

Все основные настройки проекта Django. Такие, как конфигурация баз данных, установленные приложения, настройки статических файлов и многое другое, 
производились в файле *settings.py*.

#### Импорт необходимых модулей:
````
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(verbose=True)
````
Перечень производимых настроек:
 - `SECRET_KEY = os.getenv("SECRET_KEY")` — импорт секретного ключа из переменной окружения *.env*;
 - `DEBUG = True if os.getenv("DEBUG") == "True" else False` — включение или отключение режим отладки. импорт из переменной окружения *.env*;
 - `DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("NAME"),
            "USER": os.getenv("USER"),
            "PASSWORD": os.getenv("PASSWORD"),
            "HOST": os.getenv("HOST"),
            "PORT": os.getenv("PORT"),
        }
      }` — настройки базы данных. Настройки импортированы из переменной окружения *.env*;
 - `ALLOWED_HOSTS = ["*"]` — список доменных имен, которые могут обслуживаться приложением. При отгрузках на сервере добавляется ваш домен. В данном проекте стоит звёздочка, что означает доступно всем;
 - `INSTALLED_APPS = [
    ...,
    "crispy_forms",
    "crispy_bootstrap5",
    "catalog",
    "blog",
    "users",
    "django_countries",
    "django_cleanup.apps.CleanupConfig",]` — содержит список всех приложений, активированных в проекте;

 - `LANGUAGE_CODE = "ru"` — устанавливает основной язык проекта;
 - `TIME_ZONE = "Europe/Moscow"` — устанавливает часовую зону для проекта. В данном проекте установленна зона для московского времени;
 - `STATICFILES_DIRS = (BASE_DIR / "static",)` — это список директорий на диске, из которых подгружаются статические файлы;

 - CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
 - CRISPY_TEMPLATE_PACK = "bootstrap5" — параметры для настройки стилизации в проекте;

 - `MEDIA_URL = "/media/"` — содержит информацию о URL для доступа к медиафайлам;
 - `MEDIA_ROOT = BASE_DIR / "media"`  — это директория на диске, где хранятся медиафайлы, загружаемые пользователями; 
 - `EMAIL_HOST = os.getenv("EMAIL_HOST")` — импорт адреса SMTP-сервера из переменной окружения *.env*;
 - `EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")` — импорт адреса электронной почты из переменной окружения *.env*; 
 - `EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")` — импорт ключа приложения для отправки писем с адреса электронной почты из переменной окружения *.env*; 
 - `EMAIL_PORT = os.getenv("EMAIL_PORT")` — порт SMTP-сервера для отправки электронных писем;
 - `EMAIL_USE_TLS = True if os.getenv("EMAIL_USE_TLS") == "True" else False` — использование TLS для безопасной передачи данных между клиентом и сервером для отправки электронных писем;
 - `EMAIL_USE_SSL = True if os.getenv("EMAIL_USE_SSL") == "True" else False` — использование SSL для безопасной передачи данных между клиентом и сервером для отправки электронных писем;
 - `EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")` — встроенный бэкенд для отправки электронных писем в Django, который работает через сервер Simple Mail Transfer Protocol (SMTP).;
 - `DEFAULT_FROM_EMAIL = EMAIL_HOST_USER` — адреса электронной почты используемой для отправки писем по умолчанию;

 - `AUTH_USER_MODEL = 'users.User'` — указывает используемую модель пользователя;

 - `LOGIN_REDIRECT_URL = "catalog:catalog"` — задает URL-адрес, на который будет перенаправлен пользователь после успешного входа в систему;
 - `LOGOUT_REDIRECT_URL = "catalog:catalog"` — задает URL-адрес, на который будет перенаправлен пользователь после выхода из системы;

 - `LOGIN_URL = "users:login"` — настройка URL перенаправления не авторизованных пользователей;

 - `COUNTRIES_FIRST_AUTO_DETECT = True`
 - `COUNTRIES_FIRST = ['RU',]` — настройки выборки при заполнении поля указывающего страну

Остальные настройки были уставлены по умолчанию.

#### Первичные настройки также включают в себя создание БД в ручном режиме. Для создания БД и работы данного проекта используется СУБД PostgreSQL.
#### Для создания БД в СУБД PostgreSQL используйте команду: CREATE DATABASE name_database(имя вашей БД)
#### Также в проекте представлен файл *.env.sample* который вам нужно переименовать в *.env* и указать в нём свои значения:
*SECRET_KEY = секретный ключ, используемый для криптографических подписей.*
*DEBUG = режим отладки. Включен (True), Выключен (False)*
*NAME = имя вашей базы данных.*
*USER = имя пользователя PostgreSQL.*
*PASSWORD = пароль пользователя PostgreSQL.*
*HOST = адрес сервера базы данных.*
*PORT = порт, на котором работает PostgreSQL, обычно 5432*

*EMAIL_HOST=#адрес SMTP-сервера*
*EMAIL_HOST_USER=#адрес вашей электронной почты*
*EMAIL_HOST_PASSWORD=#пароль, сгенерированный в аккаунте вашей почты для доступа приложения к рассылке писем от вашего имени*
*EMAIL_PORT=#порт SMTP-сервера*
*EMAIL_USE_TLS=#включает использование TLS для шифрования соединения. Включен (True), Выключен (False)*
*EMAIL_USE_SSL=#включает использование SSL для шифрования соединения. Включен (True), Выключен (False)*
*EMAIL_BACKEND=#бэкенд для отправки писем*

## Создание и регистрация приложения 
Для создания нового приложения в проекте Django использовалась команда:

`python manage.py startapp catalog`

В данном проекте было создано приложение с именем *catalog*, *blog* и *users*.

- в приложении *catalog* описана основная логика работы интернет магазина и работа с продуктами;
- в приложении *blog* описана логика работы дополнительного сервиса новостей интернет магазина;
- в приложении *users* описана логика регистрации и авторизации пользователей;

После создания приложения Django создал директорию с рядом файлов и поддиректорий. 

После создания приложения оно было зарегистрировано в проекте. Это было выполнено с помощью добавления имени приложения в список 
`INSTALLED_APPS = [
    ...,
    "catalog",
    "blog",
    "users"]` в файле settings.py.

## Создание контроллеров
В проекте реализованны как контроллер FBV(функциональное представление) так CBV(классовое представление), которые обрабатывают GET и POST запрос и возвращать HTML-страницы.

Контроллеры FBV(функциональное представление) реализованы в приложении *catalog*, но не используются в проекте. 
Они были закомментированны в отдельные строки.

#### Импорт необходимых модулей:

В приложении *catalog*

- `from typing import Any`
- `from django.views.generic.edit import CreateView, View`
- `from django.views.generic import ListView, TemplateView, DetailView`
- `from django.urls import reverse_lazy`
- #from django.core.paginator import Paginator - импорт класса для настройки пагинации. Используется в FBV.
- `from django.http import HttpRequest`
- `from django.shortcuts import render, get_object_or_404, get_list_or_404`
- `from catalog.forms import ProductForm`
- `from catalog.models import Product, Contacts, Category`

В приложении *blog*

- `import os`
- `from typing import Any`
- `from django.urls import reverse_lazy`
- `from django.views.generic import ListView, DetailView`
- `from django.views.generic.edit import CreateView, UpdateView, DeleteView`
- `from dotenv import load_dotenv`
- `from blog.models import Article`
- `from blog.forms import ArticleForm`
- `from blog.utils import send_email_tu_user`

#### Создание функций-контроллеров:

В приложении *catalog*

*Контроллер принимающий GET запрос и возвращающий представление главной страницы проекта.*

#`def index(request: HttpRequest) -> Any:
    return render(request, "catalog/index.html")`

*Контроллер принимающий GET и POST запросы, и возвращающий представление страницы с контактами.*

#`def contacts(request: HttpRequest) -> Any:
    if request.method == "POST":
        name = request.POST.get("name")`
        *генерация HTML-кода при POST-запросе(заполнение и отправка формы)*
        `return render(request, "catalog/message.html", {"name": name})`
    *генерация HTML-кода при GET-запросе*
    `return render(request, "catalog/contacts.html")`

#### Создание классов-контроллеров:
В файле *views.py* приложений созданы CBV, которые являются контроллерами. 
CBV (Class-Based Views) — это способ определения и обработки представлений в Django с помощью классов.

Django предоставляет механизм дженериков (Generic Class-Based Views), 
который позволяет быстро и эффективно создавать контроллеры для выполнения типичных задач, таких как создание, чтение, 
обновление и удаление объектов (CRUD-операции).

CBV в приложении *catalog*

```
class CatalogView(ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу с товарами."""

    model = Product  # определяем модель
    template_name = "catalog/index.html"  # определяем шаблон
    context_object_name = "page_object"  # определяем переменную для использования в шаблоне
    paginate_by = 6  # определяем количество продуктов на странице


class ContactView(View):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу с контактами."""

    def get(self, request: HttpRequest) ->Any:
        """Метод генерации HTML-кода при GET-запросе (страницы Контактов)"""
        context = {"contact": get_object_or_404(Contacts)}
        return render(request, "catalog/contacts.html", context)

    def post(self, request: HttpRequest) ->Any:
        """Метод генерации HTML-кода при POST-запросе(при заполнении и отправке формы).
        В методе передаются дополнительные данные об имени пользователя заполнившего форму"""
        name = request.POST.get("name")
        return render(request, "catalog/message.html", {"name": name})
```

CBV в приложении *blog*

```
class ListArticles(ListView):
    """Классовое представление принимающее GET запрос и возвращающее страницу со статьями блога,
    начиная с последней опубликованной статьи."""

    model = Article  # определяем модель
    template_name = "blog/blog.html"  # определяем шаблон
    context_object_name = "blogs"  # определяем переменную для использования в шаблоне

    def get_queryset(self) -> Any:
        """Переопределённый метод 'get_queryset'.
        Метод отбирает только те статьи у которых метод публикации равин 'True'."""

        return super().get_queryset().filter(publication=True)


class CreateArticles(CreateView):
    """Классовое представление принимающее GET и POST запрос и возвращающее страницу для добавления статьи."""

    model = Article  # определяем модель
    form_class = ArticleForm  # указываем форму
    template_name = "blog/add_article.html"  # определяем шаблон
    success_url = reverse_lazy("blogs:blogs")  # определяем URL-адрес для перехода
```

В приложении *blog* модуля *utils.py* была реализованна функция отправки сообщения на указанный в переменной `EMAIL_USER`
адрес электронной почты:

```
from django.conf import settings
from django.core.mail import send_mail


def send_email_tu_user(mail: str, subject: str, message: str) -> None:
    """Функция для отправки писем.
    Если в settings.py не настроен доступ к EMAIL_HOST_USER и EMAIL_HOST_PASSWORD, работа сервиса не прервётся."""
    try:
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [mail])
    except Exception as e:
        print(e)
```

Полную реализацию контроллеров вы можете посмотреть в модулях *views.py* которые расположены в корневых папках приложений.

## Настройка маршрутизации
При создании проект Django, в корневой директории проекта создается файл 
*urls.py* Этот файл первичен и управляет основными маршрутами вашего проекта.

Для более правильной организации проекта в директории приложения был создан отдельный файл *urls.py* в котором были описаны маршруты работы данного приложения.
После чего с использованием пространства имен они были перенесены в основной файл маршрутизации проекта *config/urls.py*.

#### Определение маршрутов в файле приложения

Маршруты определяются в списке `urlpatterns`, который связывает URL-шаблоны с соответствующими функциями контроллеров описанных выше.

Импорт необходимых модулей:
- `from django.urls import path`
- `from catalog import views`
- `from catalog.apps import CatalogConfig`

Определение пространства имен:

`app_name = CatalogConfig.name`
Задает пространство имен для всех маршрутов в файле *catalog/urls.py*. В данном случае пространство имен будет называться `catalog`.

Определение списка urlpatterns:

`urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("catalog/contacts/", views.ContactView.as_view(), name="contacts"),
    ]`

URL-путь `""` и `"contacts/"` — это части URL, которые будут использоваться для доступа к маршруту.

Контроллер `views.CatalogView.as_view()` и `views.ContactView.as_view()` — классы-контроллеры, которые будут выполнены при обращении к указанным путям.

Имя маршрута `name="index"` и `name="contacts"` — имена маршрутов, которые используются в шаблонах при перенаправлении.

#### Включение пространства имен в основной файл маршрутизации проекта *config/urls.py*
В основном файле *config/urls.py* проекта используется функция `include` и указать параметра `namespace`.

Импорт необходимых модулей:
- `from django.contrib import admin`
- `from django.urls import include, path`
- `from django.conf import settings` 
- `from django.conf.urls.static import static`

Определение списка urlpatterns:

`urlpatterns = [path("admin/", admin.site.urls),
               path("", include("catalog.urls", namespace="catalog")),
               path("", include("blog.urls", namespace="blogs")),
               ]`

Строка `path("", include("catalog.urls", namespace="catalog"))` включает URL-шаблоны из файла *catalog/urls.py* и связывает их с пространством имен 'catalog'.

Строка `path("", include("blog.urls", namespace="blogs"))` включает URL-шаблоны из файла *blog/urls.py* и связывает их с пространством имен 'blog'.

Использование пространства имен позволяет группировать маршруты и избегать конфликтов имен.

Добавление адреса ведущего к расположению медиа файлов.
`if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`

Эта настройка позволяют серверу разработки обрабатывать и выводить загруженные файлы через URL-адрес, указанный в 
*MEDIA_URL*.

## Создание моделей
Модели всегда создаются в специальном файле *models.py*, который располагается в каждом приложении и автоматически генерируется при создании приложения.

Импорт необходимых модулей:
- `from django.db import models`

Пример создания класса представляющего модель:
````
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
````

## Миграции
Миграции в Django — это механизм, который позволяет автоматически создавать и обновлять структуру базы данных на 
основе изменений в определении моделей (Models) приложения.

После определения модели, создаётся миграция, которая зафиксирует эти изменения. 
Для этого используется команда:

`python manage.py makemigrations`

Эта команда анализирует изменения в моделях и создает файлы миграций. 
Файлы миграций содержат инструкции для базы данных о том, как создать или изменить таблицы для хранения данных.

Миграции хранятся в специальных файлах внутри каждой директории приложения в папке 
*migrations*. 

Пример содержимого файла миграции:
````
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Наименование")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "db_table": "category",
                "ordering": ["name"],
            },
        ),
````

После создания миграций применяется к базе данных. 
Это делается с помощью следующей команды:

`python manage.py migrate`

Команда выполняет SQL-запросы, которые соответствуют вашим миграциям, и обновляет структуру базы данных.

## Настройка админки
Админка предоставляет простой механизм для управления данными.

Чтобы получить доступ к админке, создаётся суперпользователь.

Для создания суперпользователя используется следующая команда:

`python manage.py createsuperuser`

При выполнении этой команды указывается имя пользователя и пароль. Адрес электронной почты является опциональным параметром.

Пример создания суперпользователя:
````
Username (leave blank to use '...'): admin
Email address: 
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
````

После создания суперпользователя можно войти в админку по адресу сайта с добавлением 
*/admin/* в конце URL, при этом предварительно запустив сервер разработки. Например:

http://127.0.0.1:8000/admin/

Для настройки отображения данных моделей в админке была выполнена их регистрация и отображение в файле *admin.py*:

Импорт необходимых модулей:
- `from django.contrib import admin`
- `from catalog.models import Category, Product, Contacts`

Регистрация моделей в админке:
````
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс регистрации и настройки отображения модели 'Category' в админке"""
````

Настройка отображения:
````
    list_display = (
        "pk",
        "name",
    )
````

## Работа с Django shel
Для первоначального заполнения базы данных использовался консольный инструмент *Django shel*.

Чтобы Django shell был удобным в использовании, дополнительно был установлен пакет *ipython*.
Установка покета производилась через команду *poetry add ipython*

После установки *Django shell* был запущен с использованием *IPython*:

`python manage.py shell -i ipython`

Далее производилось работа в Django shel. Были выполнены импорты моделей вводились команд для создания сущностей и заполнения БД 
с использованием менажера запросов `objects`.
Скриншоты вводимых команд можно посмотреть в папке [screenshots](screenshots).

Для выхода из Django Shell используется команда: `exit()`, `quit()`, или сочетание клавиш Ctrl + D или Ctrl + Z.

## Создание фикстур
Фикстуры — это способ предварительно заполнить БД данными.

Перед созданием фикстур сначала было добавлено несколько записей в базу данных, через Django shell.
После этого данные были экспортированы в файлы фикстур при помощи команды:

- `python -Xutf8 manage.py dumpdata catalog.Category --output catalog/category_fixture.json --indent 4`
- `python -Xutf8 manage.py dumpdata catalog.Product --output catalog/product_fixture.json --indent 4`
- `python -Xutf8 manage.py dumpdata blog.Article --output blog/article_fixture.json --indent 4`

В результате выполнения данных команд бы ли получены *json* файлы:
- *[category_fixture.json](catalog/management/commands/category_fixture.json)*
- *[product_fixture.json](catalog/management/commands/product_fixture.json)*
- *[article_fixture.json](blog/article_fixture.json)*

Расположенные в корневой папке приложения *catalog* и *blog*
Для загрузки данных из фикстур в базу данных использовалась команда:

`python manage.py loaddata catalog/product_fixture.json --ignorenonexistent`

Данная команда импортирует данные из файла фикстуры, создавая объекты на основе экспортированных данных.

В этом проекте она использовалась в кастомных командах.

`call_command("loaddata", "catalog/product_fixture.json", "--ignorenonexistent")`

## Создание кастомных команд
Для повторного заполнения БД данными были реализованны кастомные команды.
Кастомные команды полезны для выполнения задач, которые часто повторяются или требуют автоматизации.

Для создания кастомной команды были выполнены следующие шаги:

Создан пакет *management* в приложении *catalog* и *blog*, в нем создан пакет *commands*.
Создан файл команды внутри директории *commands*.

    catalog/
    └───management/
        ├───__init__.py
        └───commands/
            ├───__init__.py
            └───add_catalog.py
Написан код команды, унаследовавшись от класса `BaseCommand`:

Импорт необходимых модулей:
- `from django.core.management import call_command`
- `from django.core.management.base import BaseCommand`
- `from django.db import connection`
- `from typing import Any`
- `from catalog.models import Category, Product`

Написан код команды:
````
class Command(BaseCommand):
    help = "Добавление категорий и продуктов тестирования в базу данных"

    def handle(self, *args: Any, **options: Any) -> None:
        """Метод добавления данных в БД"""
        
        Product.objects.all().delete()  # предварительное удаление данных из таблицы product перед загрузкой новых
        Category.objects.all().delete()  # предварительное удаление данных из таблицы category перед загрузкой новых
        ...
        
````
Остальная часть кода описана в файле [add_catalog.py](catalog/management/commands/add_catalog.py) приложения *catalog*, 
и в файле [add_catalog.py](catalog/management/commands/add_catalog.py) приложения *blog*.

После создания кастомной команды она была вызвана с помощью команды:

- `python manage.py add_catalog`
- `python manage.py add_article`

## Создание шаблонов
Для создания шаблонов HTML в приложении создана папка *templates*, внутри которой создана — папка с именем приложения:
`catalog/templates/catalog`

Затем в этой папке были созданы файл шаблона:
+ *base.html* - Базовый шаблон, который служит основой для других шаблонов;
+ *index.html* - шаблон представляющий главную страницу приложения;
+ *contacts.html* - шаблон представляющий страницу контактов;
+ *message.html* - шаблон представляющий страницу ответа от сервиса о принятии формы;
+ *header.html* - подшаблон представляющий элемент главного меню приложения использующийся во всех шаблонах;
+ *add_product.html* - шаблон представляющий страницу добавления продукта в ассортимент приложения;
+ *product_added.html* - шаблон представляющий страницу ответа от сервиса об удачном добавлении продукта;
+ *product_item.html* - шаблон представляющий страницу содержащую информацию о конкретном товаре;
+ *product_category.html* - шаблон представляющий страницу с товарами по категориям;
+ *delete_product.html* - шаблон представляющий страницу о подтверждении удаления продукта;

`blog/templates/blog`

Затем в этой папке были созданы файл шаблона:
+ *base.html* - Базовый шаблон, который служит основой для других шаблонов;
+ *blog.html* - шаблон представляющий главную страницу приложения;
+ *delete_article.html* - шаблон представляющий страницу о подтверждении удаления статьи;
+ *header.html* - подшаблон представляющий элемент главного меню приложения использующийся во всех шаблонах;
+ *add_article.html* - шаблон представляющий страницу добавления продукта в ассортимент приложения;
+ *article.html* - шаблон представляющий страницу содержащую информацию о конкретной статье;

При создании шаблонов использовались:

шаблонные теги Django:
+ `{% if %}` - тег позволяет добавлять условия в шаблон;
+ `{% for %}` - тег используется для перебора элементов в списке или другом итерируемом объекте;
+ `{% url %}` - тег используется для динамического построения URL-адресов внутри шаблонов;

и шаблонные фильтры Django:
+ `|truncatechars:100` - фильтр который сокращает текст переменной до 100 символов;
+ `|date:"d M Y"` - фильтр который форматирует дату в заданном формате.

Также были подключены статические файлы.

## Настройка и добавление статики
В корне проекта создана папка *static*, в которой содержатся поддиректории для различных типов статических файлов — таких, как: *css* и *js*.
Эти поддиректории обеспечивают доступ и управление статическими файлами с расширением *.CSS* и *.JS*.

В проекте используются готовые стили [*Bootstrap*](https://getbootstrap.com/docs/5.3/getting-started/download/).
Которые были скачены, распакованы и скопированы в ранее созданные поддиректории *css* и *js*.

#### Подключение статики в шаблонах
Для подключения статических файлов к шаблону вручную используются прямые пути.

Пример: подключение статического CSS-файла
```
<head>
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
</head>
```

Пример: подключение статического JS-файла
```
<body>
<script type="text/javascript" src="/static/js/script.js"></script>
</body>
```

Для отображения растровых изображений был описан дополнительный шаблонный фильтр, у определяющий путь до изображений.
Фильтр был описан в директории *templatetags* в файле *my_tags.py*:

````
from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f"/media/images/{path}"
    return "#"
````
Далее данный фильтр был добавлен во все шаблоны, где производилась вставка изображения.

Пример добавления фильтра в шаблоны:

`{% load my_tags %}`

Пример: вставка статического изображения
`<img src="{{ product.image | media_filter}}"`

## Создание и настройка форм
Создание и описание форм было выполнено в дерриктори каждого отдельного приложения в модуле *forms.py*.
Такой подход помогает организовать код и сделать его более читаемым и структурированным.

Для создания форм использовался класс *ModelForm* который позволяет автоматически генерировать форму на основе модели.

Импорт необходимых модулей:
```
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product
```
Основные параметры в ModelForm:

- *model* — ссылка на модель, на основе которой будет создана форма;
- *fields* — список полей модели, которые будут включены в форму.

В формах была описана логика валидации полей с использованием исключения *ValidationError*.

*ValidationError* — это исключение, которое выбрасывается, если данные не проходят валидацию. Оно используется для указания, 
что данные формы некорректны, и включает в себя сообщения об ошибках, которые будут отображены пользователю.

Стилизация форм выполнена в методе *init*, в котором настраиваются виджеты (*widget*) с использованием стилей *Bootstrap*.

Пример реализации формы в приложении *catalog*:
```
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
```

## Установка
Чтобы работать с проекта необходимо:
1. Загрузить проект в IDE через инструмент *'clone repository'* или команду `git clon`
   используя ключ: 
    - GitHub CLI: `gh repo clone L-Ev-Vi/Project_4` для работы из командной строки ОС;
    - или HTTPS: `https://github.com/L-Ev-Vi/Project_4.git`;
2. Установить зависимости проекта, выполнив команду `poetry install`;
3. Скачать БД [PostgreSQL](https://www.python.org/downloads/) для вышей ОС;
4. Выполнить установку PostgreSQL:
   - инструкцию по установке на [Windows](https://www.youtube.com/watch?v=TrDBb1zY2SM);
   - [macOS](https://www.youtube.com/watch?v=snLQ6GsxnLk);
   - [Linux](https://www.youtube.com/watch?v=FcTRbMFNdlU);

## Тестирование

## Запуск проекта
После клонирования репозитория, настройки виртуального окружения и установки необходимых зависимостей, рекомендуется заполнить БД
первичными данными и создать суперпользователя(администратора сайта) используя следующие команды:
- `python manage.py add_catalog` (Windows) - добавление первичных продуктов в каталог товаров
- `python manage.py add_blog` (Windows) - добавление первичных статей в блог магазина
- `python manage.py createadmin` (Windows) - создание суперпользователя (логин: `admin@mail.ru`, пароль: `asd1234zxc`)
, данные команды можно пропустить и сразу произвести запуск веб-приложения. 

Для запуска веб-сервиса, в терминале командной строки введите одну из команд:
- на Windows через *Terminal:* `python manage.py runserver`
- на iOS через *a-Shell:* `python3 manage.py runserver`
- на Linux через *Linux Terminal:* `python3 manage.py runserver`

После успешного запуска программы вы увидите сообщение похожее на это:

*Django version 6.0.2, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.*

Это будет означать, что сервер запущен с вашего компьютера, а ссылка `http://127.0.0.1:8000/` ,будет указывать адрес ведущий на главную страницу веб-приложения, 
которую можно будет открыть в браузере и проверить работоспособность сервиса.

Для остановки работы сервиса необходимо нажать комбинацию клавиш `Ctrl + C` после чего сервер остановится и веб-приложение, завершит свою работу.

## Команда проекта
- Евгений Лобачёв(GitHub: L-Ev-Vi) — студент курса `Python — разработчик`