# Generated by Django 4.2.3 on 2023-08-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_advertisement_image_alter_company_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetails',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='الوصف المختصر'),
        ),
    ]
