# Generated by Django 5.1.2 on 2024-10-11 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_merchantitem_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 11, 19, 7, 52, 156395, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='minlevel',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 11, 19, 7, 52, 156943, tzinfo=datetime.timezone.utc)),
        ),
    ]
