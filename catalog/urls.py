from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("product_item/<int:product_id>/", views.product_item, name="product_item"),
    path("add_product/", views.add_product, name="add_product"),
]
