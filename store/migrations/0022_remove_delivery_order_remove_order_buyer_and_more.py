# Generated by Django 4.0.5 on 2022-07-26 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_purchase_detail_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='drop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='season',
        ),
        migrations.RemoveField(
            model_name='order',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
        migrations.DeleteModel(
            name='Drop',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
