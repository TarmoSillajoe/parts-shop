# Generated by Django 5.1.1 on 2024-10-07 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_merchantitem_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 7, 11, 9, 2, 652824, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='minlevel',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 7, 11, 9, 2, 652824, tzinfo=datetime.timezone.utc)),
        ),
    ]