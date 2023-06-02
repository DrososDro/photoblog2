from .models import Article


def recent_articles_footer(request):
    recent_articles = Article.objects.all()[:2]

    return dict(recent_articles=recent_articles)
