# Generated by Django 3.2.8 on 2022-02-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_timelinemodel_members'),
        ('register', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_timeline',
            field=models.ManyToManyField(blank=True, related_name='favorite_timeline', to='app.TimelineModel', verbose_name='お気に入りのタイムライン'),
        ),
    ]
