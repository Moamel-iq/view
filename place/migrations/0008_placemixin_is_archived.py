# Generated by Django 4.2.3 on 2023-08-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_alter_placemixin_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='placemixin',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='تم الأرشفة'),
        ),
    ]