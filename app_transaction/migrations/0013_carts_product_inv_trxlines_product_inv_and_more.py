# Generated by Django 4.2.3 on 2023-08-28 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0004_alter_productinventories_table'),
        ('app_transaction', '0012_alter_trxlines_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='product_inv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_product.productinventories', verbose_name='Produt Detail Key'),
        ),
        migrations.AddField(
            model_name='trxlines',
            name='product_inv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_product.productinventories', verbose_name='Produt Detail Key'),
        ),
        migrations.AddField(
            model_name='wishlists',
            name='product_inv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_product.productinventories', verbose_name='Produt Detail Key'),
        ),
    ]
