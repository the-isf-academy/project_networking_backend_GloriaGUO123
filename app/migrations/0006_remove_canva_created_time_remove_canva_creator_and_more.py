# Generated by Django 5.1.2 on 2024-10-17 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_canva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canva',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='canva',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='canva',
            name='popularity_percentage',
        ),
        migrations.RemoveField(
            model_name='canva',
            name='time_period',
        ),
        migrations.RemoveField(
            model_name='canva',
            name='view',
        ),
    ]