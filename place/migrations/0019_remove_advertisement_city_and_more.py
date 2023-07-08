# Generated by Django 4.2.3 on 2023-07-08 16:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0018_remove_advertisement_place_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='city',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='country',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='link',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='location',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='object_id',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 7, 8, 16, 50, 23, 176795, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='place.placemixin', verbose_name='المكان'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='short_description',
            field=models.CharField(default=datetime.datetime(2023, 7, 8, 16, 50, 48, 581909, tzinfo=datetime.timezone.utc), max_length=100, verbose_name='الوصف المختصر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='الرابط'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 8, 16, 50, 52, 46470, tzinfo=datetime.timezone.utc), verbose_name='تاريخ النهاية'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='advertisements', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 8, 16, 50, 54, 634774, tzinfo=datetime.timezone.utc), verbose_name='تاريخ البداية'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default=datetime.datetime(2023, 7, 8, 16, 50, 57, 844506, tzinfo=datetime.timezone.utc), max_length=50, verbose_name='العنوان'),
            preserve_default=False,
        ),
    ]
