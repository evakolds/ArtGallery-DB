# Generated by Django 3.1.4 on 2020-12-27 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20201227_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 18, 58, 2, 204747), verbose_name='date booked'),
        ),
    ]
