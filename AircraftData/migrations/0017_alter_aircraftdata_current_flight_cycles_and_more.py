# Generated by Django 4.2.7 on 2024-05-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AircraftData', '0016_remove_aircraftdata_aircraft_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftdata',
            name='current_flight_cycles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftdata',
            name='current_flight_hours',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enginedetails',
            name='aircraft_input',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AircraftData.aircraftdata'),
        ),
    ]