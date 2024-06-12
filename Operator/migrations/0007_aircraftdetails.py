# Generated by Django 4.2.7 on 2024-03-09 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0006_alter_operatorinput_num_aircrafts'),
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_type', models.CharField(max_length=100)),
                ('production_date', models.DateField()),
                ('operator_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operator.operatorinput')),
            ],
        ),
    ]
