# Generated by Django 4.2.3 on 2023-09-05 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0018_trxheaders_courier_trxheaders_courier_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxheaders',
            name='estimation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
