# Generated by Django 4.2.7 on 2024-04-25 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AircraftData', '0007_aircraftdata_aircraft_name'),
        ('AMP', '0009_exceldata_aircraft_amp'),
    ]

    operations = [
        migrations.AddField(
            model_name='dueclearance',
            name='Aircraft_Amp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AircraftData.aircraftdata'),
        ),
    ]
