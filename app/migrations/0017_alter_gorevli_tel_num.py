# Generated by Django 4.1.5 on 2023-01-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_gorevli_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gorevli',
            name='tel_num',
            field=models.IntegerField(max_length=10),
        ),
    ]
