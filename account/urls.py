from django.urls import path
from . import views


urlpatterns = [
    path("artists/all-artists/", views.AllArtists.as_view(), name="all-artists"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("artist/<str:pk>", views.SingleArtist.as_view(), name="artist"),
]
