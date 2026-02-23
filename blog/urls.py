from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", views.ListArticles.as_view(), name="blog"),
    path("blog/add_article/", views.CreateArticles.as_view(), name="add_article"),
    path("blog/article/<int:pk>/", views.DetailArticle.as_view(), name="article"),
    path("blog/article/update_article/<int:pk>/", views.UpdateArticles.as_view(), name="update_article"),
    path("blog/article/delete_article/<int:pk>/", views.DeleteArticle.as_view(), name="delete_article"),
]