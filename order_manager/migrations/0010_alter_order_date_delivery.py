# Generated by Django 4.0.6 on 2022-07-19 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_manager', '0009_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 12, 18, 5, 616733), verbose_name='Delivery Date'),
        ),
    ]
