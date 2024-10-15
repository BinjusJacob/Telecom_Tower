# Generated by Django 5.1.1 on 2024-10-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_generatordata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatordata',
            name='tower',
        ),
        migrations.AddField(
            model_name='generatordata',
            name='fuel_percent',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='cabin_door_lock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='cabin_door_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='clean_duct_lock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='clean_duct_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='end_of_hour',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='fuel_cap_lock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='fuel_cap_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='fuel_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='gen_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='generator_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='sensor_open',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='sensor_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generatordata',
            name='uncertainty_period',
            field=models.DateTimeField(),
        ),
    ]
