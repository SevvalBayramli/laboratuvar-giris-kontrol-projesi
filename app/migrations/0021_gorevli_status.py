# Generated by Django 4.1.5 on 2023-01-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_lab_sorumlu'),
    ]

    operations = [
        migrations.AddField(
            model_name='gorevli',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
