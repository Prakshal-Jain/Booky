# Generated by Django 3.0.8 on 2020-07-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerBooks', '0002_register_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_book',
            name='book_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
