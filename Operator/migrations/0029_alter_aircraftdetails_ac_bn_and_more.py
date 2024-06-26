# Generated by Django 4.2.7 on 2024-06-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0028_alter_aircraftdetails_aircraft_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftdetails',
            name='ac_bn',
            field=models.CharField(blank=True, default='XY000', max_length=255, null=True, verbose_name='Aircraft Block Number'),
        ),
        migrations.AlterField(
            model_name='aircraftdetails',
            name='ac_ln',
            field=models.CharField(blank=True, default='0000', max_length=255, null=True, verbose_name='Aircraft Line Number'),
        ),
        migrations.AlterField(
            model_name='aircraftdetails',
            name='ac_sn',
            field=models.CharField(blank=True, default='00000', max_length=255, null=True, verbose_name='Aircraft Serial Number'),
        ),
        migrations.AlterField(
            model_name='aircraftdetails',
            name='aircraft_name',
            field=models.CharField(default='SU-AAA', max_length=100, verbose_name='Aircraft Name'),
        ),
    ]
