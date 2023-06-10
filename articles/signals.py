from .models import MultipleImages
from minio import Minio
from django.conf import settings
from django.db.models.signals import post_delete


def remove_image(sender, instance, **kwargs):
    client = Minio(
        "minio.drosinakis.com",
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    client.remove_object("photoblockmain", f"{instance.image}")


post_delete.connect(remove_image, sender=MultipleImages)
