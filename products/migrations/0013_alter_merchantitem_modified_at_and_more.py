# Generated by Django 5.1.2 on 2024-10-24 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_merchantitem_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 19, 29, 26, 643775, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='minlevel',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 19, 29, 26, 644261, tzinfo=datetime.timezone.utc)),
        ),
    ]
