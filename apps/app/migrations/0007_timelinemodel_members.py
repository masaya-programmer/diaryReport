# Generated by Django 3.2.8 on 2022-01-14 04:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_routinemodel_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelinemodel',
            name='members',
            field=models.ManyToManyField(related_name='relate_members_timeline', to=settings.AUTH_USER_MODEL),
        ),
    ]
