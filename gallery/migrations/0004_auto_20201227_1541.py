# Generated by Django 3.1.4 on 2020-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20201227_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='painting',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]