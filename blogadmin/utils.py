import uuid
from .models import MultipleBlogImages


def multiple_blog_image_add(request, object_instance):
    images = request.FILES.getlist("account_images")
    for image in images:
        image.name = f"{uuid.uuid4()}.{image.name.split('.')[-1]}"
        image_instance = MultipleBlogImages(account=object_instance, image=image)
        image_instance.save()
