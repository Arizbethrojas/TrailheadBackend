# Generated by Django 5.1.2 on 2024-11-13 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_trip_trip_bring_trip_trip_level_trip_trip_location_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='trip',
        #     name='trip_bring',
        # ),
        # migrations.RemoveField(
        #     model_name='trip',
        #     name='trip_level',
        # ),
        # migrations.RemoveField(
        #     model_name='trip',
        #     name='trip_location',
        # ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_provided',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_type',
        ),
    ]
