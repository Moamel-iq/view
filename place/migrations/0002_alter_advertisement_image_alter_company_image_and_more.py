# Generated by Django 4.2.3 on 2023-08-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='tripimages',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='الصورة'),
        ),
    ]
