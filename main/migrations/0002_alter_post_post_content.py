# Generated by Django 5.1.1 on 2024-12-18 14:15

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=tinymce.models.HTMLField(),
        ),
    ]