from django.shortcuts import reverse
from django.views.generic import CreateView
from .forms import ReviewForm
from account.decorators import authenticated_user
from django.views.decorators import method_decorator


# Create your views here.


@method_decorator(authenticated_user, name="dispatch")
class CreateReview(CreateView):
    form_class = ReviewForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        form.instance.article_id = self.kwargs["pk"]
        return super().form_valid(form, *args, **kwargs)

    def get_success_url(self):
        return reverse(
            "article",
            kwargs={"pk": self.kwargs["pk"]},
        )
