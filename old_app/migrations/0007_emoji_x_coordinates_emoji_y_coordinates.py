# Generated by Django 5.1.2 on 2024-10-15 09:42

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_input_emoji_emoji_emoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='emoji',
            name='x_coordinates',
            field=banjo.models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='emoji',
            name='y_coordinates',
            field=banjo.models.IntegerField(default=0),
        ),
    ]
