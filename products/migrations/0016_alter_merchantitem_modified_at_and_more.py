# Generated by Django 5.1.4 on 2024-12-10 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_merchantitem_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 10, 9, 4, 39, 103351, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='minlevel',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 10, 9, 4, 39, 103815, tzinfo=datetime.timezone.utc)),
        ),
    ]
