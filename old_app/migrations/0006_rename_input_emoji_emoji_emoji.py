# Generated by Django 5.1.2 on 2024-10-15 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_emoji_x_coordinates_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emoji',
            old_name='input_emoji',
            new_name='emoji',
        ),
    ]