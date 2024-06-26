# Generated by Django 4.2.7 on 2024-05-17 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0021_rename_operator_input_aircraftdetails_airline_name_and_more'),
        ('LDND', '0016_lastdone_aircraft_name_lastdone_airline_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastdone',
            name='aircraft_name',
        ),
        migrations.RemoveField(
            model_name='lastdone',
            name='airline_name',
        ),
        migrations.AddField(
            model_name='lastdone',
            name='Aircraft_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operator.aircraftdetails'),
        ),
        migrations.AddField(
            model_name='lastdone',
            name='Airline_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operator.operatorinput'),
        ),
    ]
