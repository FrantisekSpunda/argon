# Generated by Django 3.2.9 on 2021-11-17 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20211117_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_exposure',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 19, 36, 0, 429304)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_maturity',
            field=models.DateField(default=datetime.datetime(2021, 12, 17, 19, 36, 0, 429304)),
        ),
    ]
