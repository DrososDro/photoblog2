from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import Article, MultipleImages
from .forms import AddArticleForm
from tags.models import Tag
from .utils import add_tags_too_instance, multiple_image_add
from django.utils.decorators import method_decorator
from account.decorators import authenticated_user, permisions_required

# Create your views here.


# all can see
class HomeView(ListView):
    model = MultipleImages
    template_name = "articles/home.html"


# all can see
class ArticlesView(ListView):
    model = Article
    template_name = "articles/articles.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["search"] = True
        context["search_action"] = reverse("articles")
        context["search_name"] = "q_articles"

        return context

    def get_queryset(self):
        if "q_articles" in self.request.GET:
            q_articles = self.request.GET.get("q_articles")
            tags = Tag.objects.filter(title__icontains=q_articles)
            queryset = Article.objects.distinct().filter(
                Q(title__icontains=q_articles)
                | Q(description__icontains=q_articles)
                | Q(tags__in=tags)
            )
            return queryset
        else:
            return super().get_queryset()


# all can see
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


# all can see
class ArticlesByTag(ListView):
    model = Tag
    template_name = "articles/articles.html"
    paginate_by = 4

    def get_queryset(self, **kwargs):
        # queryset = tag.article_set.all()
        # return queryset
        return Tag.objects.get(id=self.kwargs["pk"]).article_set.all()


@method_decorator(
    [
        authenticated_user,
        permisions_required(perm_list=["admin", "artist"]),
    ],
    name="dispatch",
)
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


@method_decorator(
    [
        authenticated_user,
        permisions_required(perm_list=["admin", "artist"]),
    ],
    name="dispatch",
)
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


@method_decorator(
    [
        authenticated_user,
        permisions_required(perm_list=["admin", "artist"]),
    ],
    name="dispatch",
)
class DeleteImage(DeleteView):
    model = MultipleImages
    template_name = "delete.html"
    extra_context = {"text": "This Image"}

    def get_success_url(self):
        return reverse("update-user", kwargs={"pk": self.object.pk})


@method_decorator(
    [
        authenticated_user,
        permisions_required(perm_list=["admin", "artist"]),
    ],
    name="dispatch",
)
class DeleteArticle(DeleteImage):
    model = Article
    extra_context = {"text": "This Article"}
