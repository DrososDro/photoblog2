# Generated by Django 4.2.1 on 2023-06-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='search_image', to='blogadmin.multipleblogimages'),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='footer_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer', to='blogadmin.multipleblogimages'),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='navigation_bar_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navbar', to='blogadmin.multipleblogimages'),
        ),
    ]