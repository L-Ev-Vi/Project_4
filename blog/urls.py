from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("list/", views.ListArticles.as_view(), name="blogs"),
    path("add_article/", views.CreateArticles.as_view(), name="add_article"),
    path("article/<int:pk>/", views.DetailArticle.as_view(), name="article"),
    path("article/update_article/<int:pk>/", views.UpdateArticles.as_view(), name="update_article"),
    path("article/delete_article/<int:pk>/", views.DeleteArticle.as_view(), name="delete_article"),
]
