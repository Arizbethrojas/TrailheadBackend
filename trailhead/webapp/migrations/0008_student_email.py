# Generated by Django 5.1.2 on 2025-01-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_merge_20250126_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='empty', max_length=255),
            preserve_default=False,
        ),
    ]
