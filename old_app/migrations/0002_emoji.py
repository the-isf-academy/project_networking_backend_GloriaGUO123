# Generated by Django 5.1.2 on 2024-10-14 13:20

import banjo.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_emoji', banjo.models.StringField(default='')),
                ('acess_code', banjo.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.canva')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]