# Generated by Django 4.2.6 on 2023-11-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_bidding1_bidding2_delete_bidding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding1',
            name='bid_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bidding2',
            name='bid_time',
            field=models.CharField(max_length=255),
        ),
    ]
