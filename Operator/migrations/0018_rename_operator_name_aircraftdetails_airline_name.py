# Generated by Django 4.2.7 on 2024-05-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0017_rename_operator_input_aircraftdetails_operator_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraftdetails',
            old_name='operator_name',
            new_name='Airline_Name',
        ),
    ]
