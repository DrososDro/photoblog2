from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        "artists/all-artists/",
        views.AllArtists.as_view(),
        name="all-artists",
    ),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("artist/<str:pk>", views.SingleArtist.as_view(), name="artist"),
    path(
        "update-user/<str:pk>",
        views.UpdateUser.as_view(),
        name="update-user",
    ),
    path(
        "delete-image/<str:pk>",
        views.DeleteAccountImage.as_view(),
        name="delete-image",
    ),
    path(
        "activate/<uidb64>/<token>",
        views.activate,
        name="activate",
    ),
    path(
        "admin/password_reset/",
        auth_views.PasswordResetView.as_view(template_name="account/reset_pass.html"),
        name="admin_password_reset",
    ),
    path(
        "admin/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/pass_reset_mail.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/set_password.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/reset_password_success.html"
        ),
        name="password_reset_complete",
    ),
]
