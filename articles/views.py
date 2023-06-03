from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import Article, MultipleImages
from .forms import AddArticleForm
from tags.models import Tag
from .utils import add_tags_too_instance, multiple_image_add
import uuid

# Create your views here.


class HomeView(ListView):
    model = MultipleImages
    template_name = "articles/home.html"


class ArticlesView(ListView):
    model = Article
    template_name = "articles/articles.html"
    paginate_by = 4


class SingleArticleView(DetailView):
    model = Article
    template_name = "articles/single_article.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()
        try:
            context["prev_article"] = articles.filter(
                created_at__lt=self.object.created_at
            )[0]
        except IndexError:
            pass
        try:
            context["next_article"] = articles.filter(
                created_at__gt=self.object.created_at
            ).last()
        except IndexError:
            pass

        return context


class ArticlesByTag(ListView):
    model = Tag
    template_name = "articles/articles.html"
    paginate_by = 4

    def get_queryset(self, **kwargs):
        # queryset = tag.article_set.all()
        # return queryset
        return Tag.objects.get(id=self.kwargs["pk"]).article_set.all()


class CreateArticle(CreateView):
    template_name = "articles/add_article.html"
    form_class = AddArticleForm
    success_url = reverse_lazy("articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse("create-article")
        context["button"] = "Create Article"

        return context

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        # add tags and images from the fields
        add_tags_too_instance(self.request, self.object)
        multiple_image_add(self.request, self.object)

        # return redirect("create-article")
        return redirect(self.success_url)

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        return super().form_valid(form, *args, **kwargs)


class UpdateArticle(UpdateView):
    model = Article
    template_name = "articles/add_article.html"
    form_class = AddArticleForm
    success_url = reverse_lazy("articles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse(
            "update-article",
            kwargs={
                "pk": self.kwargs["pk"],
            },
        )
        context["button"] = "Update Article"

        return context

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        # add tags and images from the fields
        add_tags_too_instance(self.request, self.object)
        multiple_image_add(self.request, self.object)

        return redirect(self.success_url)
