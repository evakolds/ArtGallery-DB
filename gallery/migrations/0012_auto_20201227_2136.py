# Generated by Django 3.1.4 on 2020-12-27 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20201227_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 21, 36, 53, 114026), verbose_name='date booked'),
        ),
    ]
