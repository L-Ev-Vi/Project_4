from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", views.CatalogView.as_view(), name="catalog"),
    path("catalog/contacts/", views.ContactView.as_view(), name="contacts"),
    path("catalog/message/", views.Message.as_view(), name="message"),
    path("catalog/product_item/<int:pk>/", views.ProductItemView.as_view(), name="product_item"),
    path("catalog/add_product/", views.AddProductView.as_view(), name="add_product"),
]
