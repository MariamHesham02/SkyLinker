# Generated by Django 4.2.7 on 2024-04-25 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AMP', '0011_rename_aircraft_amp_dueclearance_aircraft_clearance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dueclearance',
            old_name='Aircraft_Clearance',
            new_name='Aircraft_Name',
        ),
        migrations.RenameField(
            model_name='exceldata',
            old_name='Aircraft_Amp',
            new_name='Aircraft_Name',
        ),
    ]
