# Generated by Django 5.1.2 on 2024-10-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_tower_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tower',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
