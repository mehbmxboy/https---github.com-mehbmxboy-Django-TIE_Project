# Generated by Django 3.2.7 on 2021-09-16 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0027_alter_testoo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testoo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]
