# Generated by Django 4.2.7 on 2024-03-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0005_alter_operatorinput_c_no_alter_operatorinput_l_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorinput',
            name='num_aircrafts',
            field=models.IntegerField(default=1),
        ),
    ]
