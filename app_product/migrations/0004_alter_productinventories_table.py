# Generated by Django 4.2.3 on 2023-08-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0003_productinventories_delete_productinventory'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productinventories',
            table='product_inventories',
        ),
    ]