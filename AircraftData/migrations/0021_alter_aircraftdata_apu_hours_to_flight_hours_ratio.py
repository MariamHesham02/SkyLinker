# Generated by Django 4.2.7 on 2024-06-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AircraftData', '0020_alter_aircraftdata_apu_fc_alter_aircraftdata_apu_fh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftdata',
            name='apu_hours_to_flight_hours_ratio',
            field=models.FloatField(blank=True, default=0.3, null=True, verbose_name='APU FH To AC Fh Ratio'),
        ),
    ]
