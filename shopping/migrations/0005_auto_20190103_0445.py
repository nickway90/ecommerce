# Generated by Django 2.1.2 on 2019-01-03 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_cart_customers_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customers_id',
            new_name='customer',
        ),
    ]
