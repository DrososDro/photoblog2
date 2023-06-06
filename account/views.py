from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .decorators import (
    authenticated_user,
    unauthenticated_user,
    permisions_required,
)
from .models import Account, MultipleAccountImages
from .admin import UserCreationForm
from django.urls import reverse, reverse_lazy
from .forms import UserModelForm
from .utils import multiple_account_image_add

# Create your views here.


# all can see
class AllArtists(ListView):
    model = Account
    paginate_by = 4
    template_name = "account/all_artists.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["search"] = True
        context["search_action"] = reverse("all-artists")
        context["search_name"] = "q_artists"

        return context

    def get_queryset(self):
        if "q_artists" in self.request.GET:
            q_artists = self.request.GET.get("q_artists")
            query = Account.objects.distinct().filter(
                Q(name__icontains=q_artists)
                | Q(
                    short_intro__icontains=q_artists,
                )
                | Q(
                    bio__icontains=q_artists,
                ),
                permissions__name="artist",
            )

            queryset = []
            for i, t in enumerate(query):
                queryset.append((True if i % 2 == 0 else False, t))
            return queryset
        else:
            queryset = []
            for i, t in enumerate(
                super().get_queryset().filter(permissions__name="artist")
            ):
                queryset.append((True if i % 2 == 0 else False, t))

            return queryset


@method_decorator(unauthenticated_user, name="dispatch")
class LoginUser(LoginView):
    template_name = "account/login_logout.html"
    next_page = reverse_lazy("home")
    extra_context = {"login": True}


@method_decorator(authenticated_user, name="dispatch")
class LogoutUser(LogoutView):
    next_page = reverse_lazy("home")


@method_decorator(unauthenticated_user, name="dispatch")
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "account/login_logout.html"
    success_url = reverse_lazy("home")


# all can see
class SingleArtist(DetailView):
    model = Account
    template_name = "account/single_artist.html"


@method_decorator(authenticated_user, name="dispatch")
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


@method_decorator(
    [
        authenticated_user,
        permisions_required(perm_list=["admin", "artist"]),
    ],
    name="dispatch",
)
class DeleteAccountImage(DeleteView):
    model = MultipleAccountImages
    template_name = "delete.html"
    extra_context = {"text": "This Picture"}

    def get_success_url(self):
        return reverse("update-user", kwargs={"pk": self.object.pk})
