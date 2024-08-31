# Generated by Django 4.2.15 on 2024-08-27 04:11

from django.db import migrations, models
import visaprocess.models


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0007_alter_visaapplication_applicant_signature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='applicant_signature',
            field=models.FileField(upload_to=visaprocess.models.applicant_signature_upload_to),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='health_ensurence',
            field=models.FileField(upload_to=visaprocess.models.health_ensurence_upload_to),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='passport_photo',
            field=models.FileField(upload_to=visaprocess.models.passport_photo_upload_to),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='travel_insurance',
            field=models.FileField(upload_to=visaprocess.models.travel_insurance_upload_to),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='user_photo',
            field=models.FileField(upload_to=visaprocess.models.user_photo_upload_to),
        ),
    ]