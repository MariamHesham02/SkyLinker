# Generated by Django 4.2.7 on 2024-03-17 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LDND', '0006_remove_dueclearance_clearance_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastdone',
            name='due_clearance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LDND.dueclearance'),
        ),
    ]