# Generated by Django 3.2.9 on 2021-11-14 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='account_number',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_exposure',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 11, 53, 5, 282096)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_maturity',
            field=models.DateField(default=datetime.datetime(2021, 12, 14, 11, 53, 5, 282096)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_city',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_country',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_dic',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_email',
            field=models.EmailField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_ic',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscriber_postal_code',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='variable_symbol',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='item',
            name='amouth',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='dph',
            field=models.FloatField(default=21, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0, null=True),
        ),
    ]
