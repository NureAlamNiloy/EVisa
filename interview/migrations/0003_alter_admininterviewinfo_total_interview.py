# Generated by Django 4.2.15 on 2024-09-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_admininterviewinfo_delete_nointerview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininterviewinfo',
            name='total_interview',
            field=models.IntegerField(default=20),
        ),
    ]