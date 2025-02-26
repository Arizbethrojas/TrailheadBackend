# Generated by Django 5.1.2 on 2024-11-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_trip_trip_bring_remove_trip_trip_level_and_more'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='trip',
        #     name='trip_bring',
        #     field=models.TextField(default='stuff'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='trip',
        #     name='trip_level',
        #     field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='trip',
        #     name='trip_location',
        #     field=models.CharField(default='here', max_length=255),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='trip',
            name='trip_provided',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_type',
            field=models.CharField(choices=[('day_trip', 'Day Trip'), ('overnight_trip', 'Overnight')], default='Day Trip', max_length=20),
            preserve_default=False,
        ),
    ]
