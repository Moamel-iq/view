# Generated by Django 4.2.3 on 2023-08-07 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('place', '0003_alter_placemixin_options_alter_placemixin_place_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='location.country', verbose_name='الدولة'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='name',
            field=models.CharField(choices=[('restaurant', 'مطعم'), ('stayplace', 'مكان اقامة'), ('cafe', 'مقهى'), ('touristplace', 'مكان سياحي'), ('mall', 'مول'), ('healthcenter', 'مركز صحي'), ('holyplace', 'مكان مقدس'), ('financial', 'مالي'), ('gasstation', 'محطة وقود'), ('entertainment', 'ترفيهي'), ('sport', 'رياضي'), ('salons', 'صالونات')], max_length=50, verbose_name='الاسم'),
        ),
    ]