# Generated by Django 3.0.8 on 2020-07-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerBooks', '0003_auto_20200709_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_book',
            name='book_image',
        ),
    ]
