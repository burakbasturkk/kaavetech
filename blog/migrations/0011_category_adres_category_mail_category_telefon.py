# Generated by Django 4.2.4 on 2023-08-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='adres',
            field=models.CharField(blank=True, default='adres', max_length=150),
        ),
        migrations.AddField(
            model_name='category',
            name='mail',
            field=models.EmailField(default='mail', max_length=254),
        ),
        migrations.AddField(
            model_name='category',
            name='telefon',
            field=models.CharField(default='telefon', max_length=11, unique=True),
        ),
    ]
