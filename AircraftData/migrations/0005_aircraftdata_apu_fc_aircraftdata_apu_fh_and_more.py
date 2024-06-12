# Generated by Django 4.2.7 on 2024-03-16 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AircraftData', '0004_alter_aircraftdata_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftdata',
            name='apu_fc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aircraftdata',
            name='apu_fh',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aircraftdata',
            name='apu_sn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aircraftdata',
            name='num_engs',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='aircraftdata',
            name='apu_hours_to_flight_hours_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftdata',
            name='current_flight_hours',
            field=models.CharField(max_length=255),
        ),
    ]