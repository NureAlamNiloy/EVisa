# Generated by Django 4.2.15 on 2024-09-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_alter_appointment_schedule_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininterviewinfo',
            name='end_time',
            field=models.TimeField(default='18:00'),
        ),
        migrations.AddField(
            model_name='admininterviewinfo',
            name='start_time',
            field=models.TimeField(default='09:00'),
        ),
    ]