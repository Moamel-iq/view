# Generated by Django 4.2.3 on 2023-08-28 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('place', '0008_alter_reviewscompany_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
