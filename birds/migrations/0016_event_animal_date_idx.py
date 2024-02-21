# Generated by Django 4.1.5 on 2024-01-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0015_event_animal_status_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['animal', 'date'], name='animal_date_idx'),
        ),
    ]
