# Generated by Django 3.1.13 on 2022-06-29 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_inventory_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='purchase_date',
        ),
    ]