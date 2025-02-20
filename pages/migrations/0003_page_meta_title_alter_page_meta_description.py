# Generated by Django 5.1 on 2025-01-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='meta_title',
            field=models.CharField(blank=True, help_text='The title that appears in search engine results (max 60 characters)', max_length=60),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description',
            field=models.TextField(blank=True, help_text='A brief description that appears in search engine results (max 160 characters)', max_length=160),
        ),
    ]
