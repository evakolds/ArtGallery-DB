# Generated by Django 3.1.4 on 2020-12-27 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20201227_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='opened_at',
            new_name='booked_at',
        ),
    ]
