# Generated by Django 4.2.3 on 2023-08-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0011_carts_quantity_wishlists_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxlines',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Price per piece'),
        ),
    ]