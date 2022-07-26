# Generated by Django 3.1.13 on 2022-06-29 05:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_inventory_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='purchase_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
