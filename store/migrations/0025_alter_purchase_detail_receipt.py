# Generated by Django 3.2.6 on 2023-09-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_purchase_detail_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_detail',
            name='receipt',
            field=models.FileField(blank=True, null=True, upload_to='receipt/'),
        ),
    ]
