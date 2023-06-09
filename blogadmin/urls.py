from django.urls import path
from .views import UpdateBlog, DeleteBlogImage


urlpatterns = [
    path("blog-admin/", UpdateBlog.as_view(), name="blog"),
    path(
        "delete-blog-image/<str:pk>",
        DeleteBlogImage.as_view(),
        name="delete-blog-image",
    ),
    # path("user-admin/", UsersView.as_view(), name="user-admin"),
]
