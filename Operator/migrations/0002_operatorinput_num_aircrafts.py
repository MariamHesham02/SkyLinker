# Generated by Django 4.2.7 on 2024-03-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorinput',
            name='num_aircrafts',
            field=models.IntegerField(default=1),
        ),
    ]