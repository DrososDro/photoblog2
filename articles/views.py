from django.db import IntegrityError
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.list import QuerySet
from .models import Article, MultipleImages
from .forms import AddArticleForm
from tags.models import Tag

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

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        add_tags = self.request.POST.get("add_tags")
        tags = add_tags.replace("#", " ").split()
        (form.tags.all())
        return super().form_valid(form, *args, **kwargs)

    """
        if add_tags:
            instance.save()
            for tag in tags:
                print(type(instance))
                try:
                    tag_instance, _ = Tag.objects.get_or_create(title=tag)
                    tag_in = Tag.objects.get(title=tag)
                    instance.tags.add(tag_in)
                    instance.save()
                    print(instance.tags.all())

                except IntegrityError:
                    pass

        form.save_m2m()

        print(instance.tags.all())
    """


"""


def create_view(request):
    form = AddArticleForm()
    if request.method == "POST":
        form = AddArticleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            print("before save")
            instance.save()
            print("save")
            return redirect("home")
    context = {"form": form}
    return render(request, "articles/add_article.html", context)
"""
