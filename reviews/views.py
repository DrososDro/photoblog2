from django.shortcuts import redirect, render, reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ReviewForm


# Create your views here.
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
