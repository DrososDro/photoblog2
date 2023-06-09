from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("articles/", views.ArticlesView.as_view(), name="articles"),
    path(
        "article/<str:pk>",
        views.SingleArticleView.as_view(),
        name="article",
    ),
    path(
        "articles/<str:pk>",
        views.ArticlesByTag.as_view(),
        name="articles_by_tags",
    ),
    path(
        "create-article/",
        views.CreateArticle.as_view(),
        name="create-article",
    ),
    path(
        "update-article/<str:pk>",
        views.UpdateArticle.as_view(),
        name="update-article",
    ),
    path(
        "delete-article-image/<str:pk>",
        views.DeleteImage.as_view(),
        name="delete-article-image",
    ),
    path(
        "delete-article/<str:pk>",
        views.DeleteArticle.as_view(),
        name="delete-article",
    ),
]
