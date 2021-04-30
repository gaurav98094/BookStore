# Generated by Django 3.2 on 2021-04-24 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210424_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, choices=[('1', 'Motivational'), ('2', 'Fiction'), ('3', 'Business'), ('4', 'Children'), ('5', 'Health'), ('6', 'Story')], max_length=32),
        ),
        migrations.AlterField(
            model_name='book',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 24, 14, 7, 38, 665483)),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_enquiry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='writerName',
            field=models.CharField(max_length=100),
        ),
    ]