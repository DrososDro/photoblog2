from django.db import models
import uuid

from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_URL(self):
        return reverse("articles_by_tags", kwargs={"pk": self.pk})
