from .models import Tag


def tags_context(request):
    tags = Tag.objects.all()

    return dict(tags=tags)
