# Generated by Django 4.2.3 on 2023-08-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0010_alter_trxlines_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='wishlists',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
