# Generated by Django 3.1.4 on 2020-12-27 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]