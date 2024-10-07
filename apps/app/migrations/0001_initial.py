# Generated by Django 3.2.8 on 2021-11-04 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateData', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('discovery', models.TextField(blank=True)),
                ('tired', models.TextField(blank=True)),
                ('dislike', models.TextField(blank=True)),
                ('happy', models.TextField(blank=True)),
                ('best', models.TextField(blank=True)),
                ('tomorrow', models.TextField(blank=True)),
                ('other', models.TextField(blank=True)),
                ('summarize', models.TextField(blank=True)),
                ('breakfast', models.ImageField(blank=True, null=True, upload_to='images/breakfast/%Y/%m/%d/%s/')),
                ('breakfastName', models.CharField(blank=True, max_length=30)),
                ('lunch', models.ImageField(blank=True, null=True, upload_to='images/lunch/%Y/%m/%d/%s/')),
                ('lunchName', models.CharField(blank=True, max_length=30)),
                ('dinner', models.ImageField(blank=True, null=True, upload_to='images/dinner/%Y/%m/%d/%s/')),
                ('dinnerName', models.CharField(blank=True, max_length=30)),
                ('snack', models.ImageField(blank=True, null=True, upload_to='images/snack/%Y/%m/%d/%s/')),
                ('snackName', models.CharField(blank=True, max_length=30)),
                ('mealEvaluation', models.CharField(blank=True, choices=[('野菜が少ない', '野菜が少ない'), ('カロリーが高い', 'カロリーが高い'), ('栄養満点', '栄養満点')], default='', max_length=30)),
                ('mealComment', models.TextField(blank=True)),
                ('condition', models.CharField(blank=True, choices=[('良好', '良好'), ('普通', '普通'), ('悪い', '悪い')], default='', max_length=30)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
