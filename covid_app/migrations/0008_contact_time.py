# Generated by Django 4.2.4 on 2023-09-10 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0007_alter_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.TimeField(default=datetime.time(11, 48, 37, 481972)),
        ),
    ]
