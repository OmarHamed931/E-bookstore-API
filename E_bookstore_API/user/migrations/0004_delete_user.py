# Generated by Django 5.1 on 2024-08-28 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
