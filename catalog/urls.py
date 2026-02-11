from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
]
