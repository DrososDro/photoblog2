# Generated by Django 4.2.1 on 2023-06-05 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_article_multipleaccountimages_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multipleaccountimages',
            name='is_profile_picture',
        ),
    ]
