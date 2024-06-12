# Generated by Django 4.2.7 on 2024-05-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0021_rename_operator_input_aircraftdetails_airline_name_and_more'),
        ('AMP', '0022_remove_exceldata_aircraft_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dueclearance',
            name='Aircraft_Name',
        ),
        migrations.AddField(
            model_name='dueclearance',
            name='Aircraft_Name',
            field=models.ManyToManyField(blank=True, to='Operator.aircraftdetails'),
        ),
    ]