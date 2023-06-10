from django.urls import path
from .views import UpdateBlog, DeleteBlogImage, UsersView, UpdateUserAdminView


urlpatterns = [
    path("blog-admin/", UpdateBlog.as_view(), name="blog"),
    path(
        "delete-blog-image/<str:pk>",
        DeleteBlogImage.as_view(),
        name="delete-blog-image",
    ),
    path("user-admin/", UsersView.as_view(), name="user-admin"),
    path("user-change/<str:pk>", UpdateUserAdminView.as_view(), name="user-change"),
]
