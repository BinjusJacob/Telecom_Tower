# Generated by Django 5.1.1 on 2024-10-14 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_remove_generatordata_tower_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatordata',
            old_name='Time',
            new_name='time',
        ),
    ]
