# Generated by Django 3.2.5 on 2021-07-09 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20210709_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 15, 52, 42, 837898)),
        ),
    ]
