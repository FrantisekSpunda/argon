# Generated by Django 3.2.9 on 2021-11-15 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20211115_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_exposure',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 17, 3, 10, 734251)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_maturity',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 17, 3, 10, 734251)),
        ),
    ]
