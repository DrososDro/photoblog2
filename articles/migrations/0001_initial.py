# Generated by Django 4.2.1 on 2023-06-06 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('reviews', models.ManyToManyField(blank=True, to='reviews.review')),
                ('tags', models.ManyToManyField(blank=True, to='tags.tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MultipleImages',
            fields=[
                ('image', models.FileField(blank=True, null=True, unique=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
