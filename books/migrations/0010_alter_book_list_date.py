# Generated by Django 3.2 on 2021-04-28 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210428_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 28, 11, 50, 59, 719189)),
        ),
    ]
