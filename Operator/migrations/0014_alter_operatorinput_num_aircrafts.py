# Generated by Django 4.2.7 on 2024-05-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Operator", "0013_alter_operatorinput_num_aircrafts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operatorinput",
            name="num_aircrafts",
            field=models.IntegerField(default=10),
        ),
    ]
