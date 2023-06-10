from django.db import models
import uuid
from django.db.models import Avg
from django.urls import reverse
from tags.models import Tag
from account.models import Account
import os


# Create your models here.
def generate_filename(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = "{}{}".format(uuid.uuid4(), extension)
    return new_filename


class Article(models.Model):
    # here cascade because we dont know
    # if the owner want to keep them or delete them
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def total_votes(self):
        return self.review_set.all().count()

    def images(self):
        return self.multipleimages_set.all()

    def average_rating(self):
        if self.total_votes() > 0:
            average_rating = self.review_set.all().aggregate(Avg("star_rating"))
            print(average_rating)
            return average_rating["star_rating__avg"]
        else:
            return 0

    def get_URL(self):
        return reverse("article", kwargs={"pk": self.id})

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset


class MultipleImages(models.Model):
    article = models.ForeignKey(
        Article,
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
