# Generated by Django 4.2.3 on 2023-07-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]