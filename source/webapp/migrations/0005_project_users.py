# Generated by Django 2.2 on 2019-11-12 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_auto_20191106_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='projects', through='webapp.Team', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]
