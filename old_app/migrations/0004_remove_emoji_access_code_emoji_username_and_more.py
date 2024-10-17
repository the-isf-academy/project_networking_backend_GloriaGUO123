# Generated by Django 5.1.2 on 2024-10-15 06:52

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_acess_code_emoji_access_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emoji',
            name='access_code',
        ),
        migrations.AddField(
            model_name='emoji',
            name='username',
            field=banjo.models.StringField(default=''),
        ),
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
        migrations.DeleteModel(
            name='Canva',
        ),
    ]