# Generated by Django 4.2.3 on 2023-08-21 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0005_trxheaders_city_name_trxheaders_country_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trxheaders',
            old_name='city',
            new_name='city_id',
        ),
        migrations.RenameField(
            model_name='trxheaders',
            old_name='country',
            new_name='country_id',
        ),
        migrations.RenameField(
            model_name='trxheaders',
            old_name='province',
            new_name='province_id',
        ),
    ]