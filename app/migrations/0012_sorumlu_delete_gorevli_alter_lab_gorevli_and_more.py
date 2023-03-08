# Generated by Django 4.1.5 on 2023-01-23 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_gorevli_lab_gorevli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorumlu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Gorevli',
        ),
        migrations.AlterField(
            model_name='lab',
            name='gorevli',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lab',
            name='sorumlu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.sorumlu'),
        ),
    ]
