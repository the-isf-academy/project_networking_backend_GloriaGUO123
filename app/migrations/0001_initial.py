# Generated by Django 5.1.2 on 2024-10-17 08:36

import banjo.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', banjo.models.StringField(default='')),
                ('username', banjo.models.StringField(default='')),
                ('x_coordinates', banjo.models.IntegerField(default=0)),
                ('y_coordinates', banjo.models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Canva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', banjo.models.IntegerField(default=0)),
                ('emojis', banjo.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.emoji')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
