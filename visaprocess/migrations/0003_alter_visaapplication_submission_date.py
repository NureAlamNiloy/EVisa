# Generated by Django 4.2.15 on 2024-09-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0002_alter_visastatus_visa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]