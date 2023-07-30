# Generated by Django 4.2.3 on 2023-07-30 02:08

import datetime
from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_alter_tripdetails_trip_details_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tripdetails',
            options={'verbose_name': 'تفاصيل الرحلة', 'verbose_name_plural': 'تفاصيل الرحلات'},
        ),
        migrations.RenameField(
            model_name='company',
            old_name='Company_name',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tripdetails',
            name='trip_days',
        ),
        migrations.RemoveField(
            model_name='tripdetails',
            name='trip_price',
        ),
        migrations.RemoveField(
            model_name='tripdetails',
            name='trip_type',
        ),
        migrations.AddField(
            model_name='trip',
            name='company_description',
            field=models.CharField(default=datetime.datetime(2023, 7, 30, 2, 8, 8, 131691, tzinfo=datetime.timezone.utc), max_length=100, verbose_name='وصف الشركة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='33.3152, 44.3661', max_length=63),
        ),
    ]