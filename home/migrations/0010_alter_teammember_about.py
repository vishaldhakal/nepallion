# Generated by Django 4.1.4 on 2023-03-18 11:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_featuredtour_banner_tour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='about',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]