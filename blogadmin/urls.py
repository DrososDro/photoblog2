from django.urls import path
from .views import UpdateBlog


urlpatterns = [path("blog/<int:pk>", UpdateBlog.as_view(), name="blog")]
