# Generated by Django 5.1.1 on 2024-10-05 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_merchantitem_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 16, 47, 30, 351360, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='minlevel',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 16, 47, 30, 351801, tzinfo=datetime.timezone.utc)),
        ),
    ]