import uuid
from tags.models import Tag
from .models import MultipleImages


def add_tags_too_instance(request, object_instance):
    add_tags = request.POST.get("add_tags")
    tags = add_tags.replace("#", " ").split()
    if add_tags:
        for tag in tags:
            tag_instance, _ = Tag.objects.get_or_create(title=tag)
            object_instance.tags.add(tag_instance)


def multiple_image_add(request, object_instance):
    images = request.FILES.getlist("images")
    for image in images:
        image.name = f"{uuid.uuid4()}.{image.name.split('.')[-1]}"
        MultipleImages.objects.create(article=object_instance, image=image)
