# Generated by Django 3.2.9 on 2021-11-15 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20211115_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_exposure',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 12, 28, 32, 675122)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_maturity',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 12, 28, 32, 675122)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='text',
            field=models.TextField(default='Put some text here for client...', max_length=256),
        ),
    ]
