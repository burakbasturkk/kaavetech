# Generated by Django 4.2.4 on 2023-08-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_category_adres_category_mail_category_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='kategori_ad', to='blog.category'),
        ),
    ]
