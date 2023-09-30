# Generated by Django 4.2.3 on 2023-08-19 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0002_remove_trxheaders_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trxheaders',
            name='trx_number',
            field=models.CharField(default='TRX', max_length=20),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('payment_num', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('payment_date', models.DateTimeField()),
                ('expired_date', models.DateTimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_transaction.trxheaders', verbose_name='Transaction Header Key')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]
