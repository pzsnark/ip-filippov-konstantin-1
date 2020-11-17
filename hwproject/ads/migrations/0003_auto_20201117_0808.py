# Generated by Django 3.1.3 on 2020-11-17 04:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0002_ad_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_up',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/ad_photos'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
