# Generated by Django 5.1.1 on 2024-10-05 16:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.BigAutoField(db_comment='primary key', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'base_item',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'branch',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(db_comment='primary key', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'merchant',
            },
        ),
        migrations.CreateModel(
            name='Props',
            fields=[
                ('props_id', models.AutoField(primary_key=True, serialize=False)),
                ('schema_def', models.JSONField(blank=True, null=True, unique=True)),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'props',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('base_item', models.ForeignKey(blank=True, db_comment='foreign key', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.baseitem')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer')),
            ],
            options={
                'db_table': 'item',
                'unique_together': {('code', 'manufacturer')},
            },
        ),
        migrations.AddField(
            model_name='baseitem',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.merchant'),
        ),
        migrations.CreateModel(
            name='MerchantItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(max_length=50)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2024, 10, 5, 16, 44, 23, 849353))),
                ('min_order', models.SmallIntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.merchant')),
            ],
            options={
                'db_table': 'merchant_item',
                'unique_together': {('merchant', 'item', 'code', 'min_order')},
            },
        ),
        migrations.CreateModel(
            name='Ean',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ean', models.CharField(max_length=13)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'db_table': 'ean',
                'unique_together': {('item', 'ean')},
            },
        ),
        migrations.CreateModel(
            name='ItemReplacement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('replacable', models.ForeignKey(db_column='replacable', on_delete=django.db.models.deletion.CASCADE, to='products.baseitem')),
                ('replacement', models.ForeignKey(db_column='replacement', on_delete=django.db.models.deletion.CASCADE, related_name='itemreplacement_replacement_set', to='products.baseitem')),
            ],
            options={
                'db_table': 'item_replacement',
                'unique_together': {('replacable', 'replacement')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='baseitem',
            unique_together={('id', 'code')},
        ),
        migrations.CreateModel(
            name='MinLevel',
            fields=[
                ('min_level_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(default=1)),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2024, 10, 5, 16, 44, 23, 849864))),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.branch')),
                ('merchant_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.merchantitem')),
            ],
            options={
                'db_table': 'min_level',
                'unique_together': {('merchant_item', 'branch')},
            },
        ),
        migrations.CreateModel(
            name='BaseItemProp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_props', models.JSONField(blank=True, db_column='props', null=True)),
                ('base_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.baseitem')),
                ('props', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.props')),
            ],
            options={
                'db_table': 'base_item_prop',
                'unique_together': {('props', 'base_item')},
            },
        ),
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.merchantitem')),
                ('return_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returnitem_return_item_set', to='products.merchantitem')),
            ],
            options={
                'db_table': 'return_item',
                'unique_together': {('item', 'return_item')},
            },
        ),
    ]