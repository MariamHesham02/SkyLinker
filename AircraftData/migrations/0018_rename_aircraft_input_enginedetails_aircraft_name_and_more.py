# Generated by Django 4.2.7 on 2024-05-13 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0021_rename_operator_input_aircraftdetails_airline_name_and_more'),
        ('AircraftData', '0017_alter_aircraftdata_current_flight_cycles_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enginedetails',
            old_name='aircraft_input',
            new_name='Aircraft_Name',
        ),
        migrations.AddField(
            model_name='aircraftdata',
            name='Aircraft_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operator.aircraftdetails'),
        ),
        migrations.AddField(
            model_name='aircraftdata',
            name='Airline_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operator.operatorinput'),
        ),
        migrations.AddField(
            model_name='enginedetails',
            name='Airline_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operator.operatorinput'),
        ),
    ]
