# Generated by Django 4.2.3 on 2023-09-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0020_alter_trxheaders_estimation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxheaders',
            name='courier_service',
            field=models.CharField(default='', max_length=20),
        ),
    ]
