# Generated by Django 5.1 on 2024-09-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_id'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(choices=[], related_name='books', to='category.category', verbose_name='categories'),
        ),
    ]
