# Generated by Django 5.1.2 on 2025-01-07 19:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0002_remove_student_email_student_user_trip_trip_bring_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_bring",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_leader",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_level",
            field=models.CharField(
                choices=[
                    ("beginner", "Beginner"),
                    ("intermediate", "Intermediate"),
                    ("advanced", "Advanced"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_location",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_provided",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_type",
            field=models.CharField(
                choices=[("day_trip", "Day Trip"), ("overnight_trip", "Overnight")],
                max_length=20,
            ),
        ),
    ]
