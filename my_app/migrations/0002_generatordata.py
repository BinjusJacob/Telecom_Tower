# Generated by Django 5.1.1 on 2024-10-13 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField()),
                ('end_of_hour', models.BooleanField(default=False)),
                ('uncertainty_period', models.CharField(max_length=100)),
                ('grid_r_ph_volt', models.FloatField()),
                ('gset_r_ph_volt', models.FloatField()),
                ('gen_status', models.CharField(max_length=100)),
                ('generator_status', models.CharField(max_length=100)),
                ('bat_volt', models.FloatField()),
                ('fuel_ltr', models.FloatField()),
                ('fuel_status', models.CharField(max_length=100)),
                ('sensor_open', models.BooleanField(default=False)),
                ('sensor_status', models.CharField(max_length=100)),
                ('cabin_door_lock', models.BooleanField(default=False)),
                ('cabin_door_status', models.CharField(max_length=100)),
                ('clean_duct_lock', models.BooleanField(default=False)),
                ('clean_duct_status', models.CharField(max_length=100)),
                ('fuel_cap_lock', models.BooleanField(default=False)),
                ('fuel_cap_status', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('tower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.tower')),
            ],
        ),
    ]
