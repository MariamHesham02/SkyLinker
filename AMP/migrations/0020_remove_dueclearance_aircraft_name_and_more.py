# Generated by Django 4.2.7 on 2024-05-13 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AMP', '0019_remove_exceldata_aircraft_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dueclearance',
            name='Aircraft_Name',
        ),
        migrations.RemoveField(
            model_name='dueclearance',
            name='Airline_Name',
        ),
        migrations.RemoveField(
            model_name='exceldata',
            name='Aircraft_Name',
        ),
        migrations.RemoveField(
            model_name='exceldata',
            name='Airline_Name',
        ),
    ]
