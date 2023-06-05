from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, ListView, CreateView
from .models import Account
from .admin import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class AllArtists(ListView):
    model = Account
    paginate_by = 4
    template_name = "account/all_artists.html"

    def get_queryset(self):
        queryset = []
        for i, t in enumerate(super().get_queryset()):
            queryset.append((True if i % 2 == 0 else False, t))

        return queryset


class LoginUser(LoginView):
    template_name = "account/login_logout.html"
    next_page = reverse_lazy("home")
    extra_context = {"login": True}


class LogoutUser(LogoutView):
    next_page = reverse_lazy("home")


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "account/login_logout.html"
    success_url = reverse_lazy("home")


class SingleArtist(DetailView):
    model = Account
    template_name = "account/single_artist.html"
