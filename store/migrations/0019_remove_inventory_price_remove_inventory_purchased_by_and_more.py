# Generated by Django 4.0.5 on 2022-06-30 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_purchase_detail_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='purchased_by',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='purchased_from',
        ),
    ]