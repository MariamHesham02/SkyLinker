# Generated by Django 4.2.7 on 2024-03-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMP', '0006_exceldata_dynamic_applicability'),
    ]

    operations = [
        migrations.CreateModel(
            name='DueClearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DY_clearance', models.IntegerField(blank=True, null=True)),
                ('FH_clearance', models.CharField(blank=True, max_length=255, null=True)),
                ('FC_clearance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Due Clearance',
            },
        ),
    ]
