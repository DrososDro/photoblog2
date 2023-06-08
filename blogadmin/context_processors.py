from .models import BlogInfo


def blog_info(request):
    blog = BlogInfo.objects.all()[0]
    return dict(blog_info=blog)
