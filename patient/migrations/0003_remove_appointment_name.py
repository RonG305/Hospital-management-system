# Generated by Django 4.1.7 on 2023-03-22 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_appointment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
    ]