# Generated by Django 4.0.5 on 2022-08-03 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220628_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_buyer',
            new_name='is_employee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_supplier',
        ),
    ]