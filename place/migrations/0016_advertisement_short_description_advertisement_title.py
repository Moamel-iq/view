# Generated by Django 4.2.3 on 2023-10-08 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0015_remove_advertisement_short_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='short_description',
            field=models.CharField(default=datetime.datetime(2023, 10, 8, 10, 39, 18, 556251, tzinfo=datetime.timezone.utc), max_length=100, verbose_name='الوصف المختصر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default=datetime.datetime(2023, 10, 8, 10, 39, 27, 102646, tzinfo=datetime.timezone.utc), max_length=50, verbose_name='العنوان'),
            preserve_default=False,
        ),
    ]
