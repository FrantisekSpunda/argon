# Generated by Django 3.2.9 on 2021-11-17 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20211115_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_exposure',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 17, 54, 13, 183946)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_maturity',
            field=models.DateField(default=datetime.datetime(2021, 12, 17, 17, 54, 13, 183946)),
        ),
    ]
