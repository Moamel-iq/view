# Generated by Django 4.2.3 on 2023-08-01 09:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_emailaccount_is_merchant_emailaccount_is_normal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilemerchant',
            options={'verbose_name': 'الملف الشخصي للتاجر ', 'verbose_name_plural': 'الملفات الشخصية للتجار'},
        ),
        migrations.CreateModel(
            name='ProfileNormal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.normaluser')),
            ],
            options={
                'verbose_name': 'الملف الشخصي',
                'verbose_name_plural': 'الملفات الشخصية',
            },
        ),
    ]