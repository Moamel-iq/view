# Generated by Django 4.2.3 on 2023-10-02 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0014_alter_socialmedia_company_alter_socialmedia_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='title',
        ),
    ]