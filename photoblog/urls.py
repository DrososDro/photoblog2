"""
URL configuration for photoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    include,
    path,
)
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.sitemaps.views import sitemap
from articles.models import Article
from account.models import Account
from django.contrib.sitemaps import Sitemap


class MySitemap(Sitemap):
    def items(self):
        # Return the queryset or list of objects to include in the sitemap
        account = Account.objects.all()
        articles = Article.objects.all()

        return list(account) + list(articles)

    def location(self, item):
        # Return the URL for each object in the queryset
        if isinstance(item, Account):
            return item.get_URL()
        elif isinstance(item, Article):
            return item.get_URL()


sitemaps = {"all_urls": MySitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("articles.urls")),
    path("users/", include("account.urls")),
    path("reviews/", include("reviews.urls")),
    path("blog_admin/", include("blogadmin.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
