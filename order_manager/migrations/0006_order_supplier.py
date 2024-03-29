# Generated by Django 4.0.6 on 2022-07-19 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_manager', '0002_alter_supplier_description_alter_supplier_name'),
        ('order_manager', '0005_remove_products_quantity_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier_manager.supplier'),
        ),
    ]
