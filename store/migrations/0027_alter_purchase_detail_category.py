# Generated by Django 3.2.6 on 2023-09-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_purchase_detail_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_detail',
            name='category',
            field=models.CharField(blank=True, choices=[('CPU', 'CPU'), ('EC10', 'EC10'), ('HDD', 'HDD'), ('Ink', 'Ink'), ('IP Camera', 'IP Camera'), ('Keyboard', 'Keyboard'), ('Laptop', 'Laptop'), ('Mobile', 'Mobile'), ('Monitor', 'Monitor'), ('Mouse', 'Mouse'), ('PABX', 'PABX'), ('Pendrive', 'Pendrive'), ('Printer', 'Printer'), ('PoE Switch', 'PoE Switch'), ('RAM', 'RAM'), ('Router', 'Router'), ('SSD', 'SSD'), ('Tab', 'Tab'), ('Toner', 'Toner'), ('UPS', 'UPS'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]
