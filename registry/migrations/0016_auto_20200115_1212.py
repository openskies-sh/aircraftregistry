# Generated by Django 3.0.2 on 2020-01-15 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0015_auto_20191218_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='flight_controller_number',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='operating_frequency',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operator',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 0, 0, tzinfo=utc)),
        ),
    ]
