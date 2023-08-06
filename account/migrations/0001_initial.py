# Generated by Django 4.2.3 on 2023-08-03 11:18

import account.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('app_version', models.CharField(max_length=100, verbose_name='رقم الاصدار التطبيق')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailAccount',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='الاسم الاول')),
                ('last_name', models.CharField(max_length=255, verbose_name='الاسم الثاني')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone_number', models.IntegerField(unique=True, verbose_name='رقم الهاتف')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='الصورة')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_merchant', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'حساب',
                'verbose_name_plural': 'حسابات',
            },
            managers=[
                ('objects', account.models.EmailAccountManager()),
            ],
        ),
    ]
