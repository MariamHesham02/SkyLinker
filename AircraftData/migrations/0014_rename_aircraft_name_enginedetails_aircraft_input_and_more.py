# Generated by Django 4.2.7 on 2024-05-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AircraftData', '0013_alter_enginedetails_aircraft_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enginedetails',
            old_name='Aircraft_Name',
            new_name='aircraft_input',
        ),
        migrations.RemoveField(
            model_name='aircraftdata',
            name='Airline_Name',
        ),
        migrations.RemoveField(
            model_name='enginedetails',
            name='Airline_Name',
        ),
        migrations.AlterField(
            model_name='aircraftdata',
            name='Aircraft_Name',
            field=models.CharField(default='SU-', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraftdata',
            name='current_flight_cycles',
            field=models.IntegerField(),
        ),
    ]