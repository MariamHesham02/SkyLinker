# Generated by Django 4.2.7 on 2024-03-16 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0009_alter_aircraftdetails_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftdetails',
            name='ac_bn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aircraftdetails',
            name='ac_ln',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aircraftdetails',
            name='ac_sn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
