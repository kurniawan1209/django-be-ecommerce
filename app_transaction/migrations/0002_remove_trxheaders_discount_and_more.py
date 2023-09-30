# Generated by Django 4.2.3 on 2023-08-19 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trxheaders',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='trxheaders',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='trxlines',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='trxlines',
            name='discount_price',
        ),
        migrations.AddField(
            model_name='trxheaders',
            name='shipping_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trxlines',
            name='cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app_transaction.carts', verbose_name='Cart Key'),
        ),
        migrations.AlterField(
            model_name='carts',
            name='wishlist',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_transaction.wishlists', verbose_name='Wishlist Key'),
        ),
        migrations.AlterField(
            model_name='trxlines',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_key', to='app_transaction.trxheaders', verbose_name='Transaction Header Key'),
        ),
        migrations.DeleteModel(
            name='Discounts',
        ),
    ]