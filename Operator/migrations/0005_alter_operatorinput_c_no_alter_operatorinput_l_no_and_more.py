# Generated by Django 4.2.7 on 2024-03-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0004_remove_operatorinput_aircraft_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorinput',
            name='C_no',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='operatorinput',
            name='L_no',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='operatorinput',
            name='num_aircrafts',
            field=models.IntegerField(default=0),
        ),
    ]
