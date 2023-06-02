from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from account.models import Account

# Create your models here.


class Review(models.Model):
    owner = models.ForeignKey(Account, models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    star_rating = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(5.0),
        ],
    )
    updated_ad = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if float(self.star_rating) < 0 or float(self.star_rating) > 5:
            self.star_rating = 0
        return super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
