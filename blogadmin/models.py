from django.db import models
import uuid


# Create your models here.
class BlogInfo(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    navigation_bar_image = models.ForeignKey(
        "MultipleBlogImages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="navbar",
    )

    footer_image = models.ForeignKey(
        "MultipleBlogImages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="footer",
    )


class MultipleBlogImages(models.Model):
    article = models.ForeignKey(
        BlogInfo,
        on_delete=models.CASCADE,
    )
    image = models.FileField(
        null=True,
        blank=True,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def image_url(self):
        if self.image:
            return self.image.url
        return ""

    def __str__(self):
        return str(self.image)
