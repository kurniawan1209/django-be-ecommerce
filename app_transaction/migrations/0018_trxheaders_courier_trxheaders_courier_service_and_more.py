# Generated by Django 4.2.3 on 2023-09-05 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0017_remove_trxheaders_country_id_trxheaders_postal_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trxheaders',
            name='courier',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='trxheaders',
            name='courier_service',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='trxheaders',
            name='estimation_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 8, 37, 19, 200103, tzinfo=datetime.timezone.utc)),
        ),
    ]