# Generated by Django 4.2.1 on 2023-06-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_multipleimages_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimages',
            name='image',
            field=models.FileField(blank=True, null=True, unique=True, upload_to=''),
        ),
    ]