# Generated by Django 4.2.14 on 2024-07-31 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0007_rename_health_information_visaapplication_travel_insurance_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visastatus',
            options={'ordering': ['update_at'], 'verbose_name_plural': 'Visa Status'},
        ),
    ]
