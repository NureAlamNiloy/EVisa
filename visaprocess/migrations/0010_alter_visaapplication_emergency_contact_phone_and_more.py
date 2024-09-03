# Generated by Django 4.2.15 on 2024-09-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0009_rename_passport_photo_visaapplication_passport_back_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='emergency_contact_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='visastatus',
            name='visa_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('schedule', 'schedule'), ('PoliceVerification', 'PoliceVerification'), ('AdminApprove', 'AdminApprove')], default='Pending', max_length=100),
        ),
    ]