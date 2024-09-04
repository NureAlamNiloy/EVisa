# Generated by Django 4.2.15 on 2024-09-04 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visaprocess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoInterview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_interview_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateField()),
                ('start_time', models.TimeField(default='9:00')),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('schedule_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='interview.scheduleslot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visa_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='visaprocess.visaapplication')),
            ],
            options={
                'unique_together': {('visa_application', 'schedule_slot')},
            },
        ),
    ]
