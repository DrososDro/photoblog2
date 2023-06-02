# Generated by Django 4.2.1 on 2023-06-02 16:01

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimages',
            name='image',
            field=models.FileField(blank=True, null=True, unique=True, upload_to=articles.models.generate_filename),
        ),
    ]
