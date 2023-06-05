from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Account, MultipleAccountImages
from .admin import UserCreationForm
from django.urls import reverse, reverse_lazy
from .forms import UserModelForm
from .utils import multiple_account_image_add

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


class UpdateUser(UpdateView):
    model = Account
    form_class = UserModelForm
    template_name = "account/user_profile.html"

    def get_success_url(self):
        return reverse("update-user", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        account = Account.objects.get(pk=self.request.user.id)
        return account

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        multiple_account_image_add(self.request, self.object)
        return redirect(self.get_success_url())
