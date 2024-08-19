# Generated by Django 4.2.7 on 2024-08-19 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visaprocess', '0005_rename_traking_id_visastatus_tracking_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateField()),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visa_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visaprocess.visaapplication')),
            ],
            options={
                'unique_together': {('visa_application', 'interview_date')},
            },
        ),
    ]