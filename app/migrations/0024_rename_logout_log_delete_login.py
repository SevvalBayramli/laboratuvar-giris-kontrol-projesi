# Generated by Django 4.1.5 on 2023-01-26 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_logout_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LogOut',
            new_name='Log',
        ),
        migrations.DeleteModel(
            name='LogIn',
        ),
    ]
