# Generated by Django 4.2.7 on 2024-06-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0027_alter_aircraftdetails_ac_bn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftdetails',
            name='aircraft_type',
            field=models.CharField(default='B737-700', max_length=100, verbose_name='Aircraft Type'),
        ),
    ]
