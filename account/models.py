from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.urls import reverse


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not name:
            raise ValueError("User must have a name")

        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_superadmin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    email = models.EmailField(unique=True, max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)

    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    permissions = models.ManyToManyField("Perm", blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    def full_name(self):
        if self.surname:
            surname = self.surname
        else:
            surname = ""

        return f"{self.name}  {surname}"

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        if self.email:
            self.email = self.email.lower()
        if self.surname:
            self.surname = self.surname.lower()
        super().save(*args, **kwargs)

    def get_URL(self):
        return reverse("artist", kwargs={"pk": self.id})


class Perm(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MultipleAccountImages(models.Model):
    article = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    image = models.FileField(
        null=True,
        blank=True,
        unique=True,
        upload_to="account",
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
