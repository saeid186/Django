# Generated by Django 4.0.1 on 2022-01-18 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
