# Generated by Django 4.1.3 on 2023-01-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_gorevli_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]