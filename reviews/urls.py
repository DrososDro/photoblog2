from django.urls import path
from .views import CreateReview

urlpatterns = [path("review/<str:pk>", CreateReview.as_view(), name="review")]
