# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class Manufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    merchant = models.ForeignKey(
        "Merchant", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = "manufacturer"
        ordering = ["name"]


class Merchant(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="primary key")
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        db_table = "merchant"
        ordering = ["name"]


class Props(models.Model):
    props_id = models.AutoField(primary_key=True)
    schema_def = models.JSONField(unique=True, blank=True, null=True)
    title = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = "props"


class BaseItem(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment="primary key")
    code = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    manufacturer = models.ForeignKey("Manufacturer", models.CASCADE)

    class Meta:
        db_table = "base_item"
        unique_together = (("id", "code"),)


class BaseItemProp(models.Model):
    props = models.ForeignKey("Props", on_delete=models.CASCADE)
    base_item = models.ForeignKey(BaseItem, on_delete=models.CASCADE)
    json_props = models.JSONField(db_column="props", blank=True, null=True)

    class Meta:
        db_table = "base_item_prop"
        unique_together = (("props", "base_item"),)


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = "branch"


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50)
    base_item = models.ForeignKey(
        BaseItem, models.SET_NULL, blank=True, null=True, db_comment="foreign key"
    )
    manufacturer = models.ForeignKey("Manufacturer", models.CASCADE)

    class Meta:
        db_table = "item"
        unique_together = (
            ("code", "manufacturer"),
            ("code", "manufacturer"),
        )
        ordering = ["code"]


class Ean(models.Model):
    id = models.BigAutoField(primary_key=True)
    ean = models.CharField(max_length=13)
    item = models.ForeignKey("Item", models.CASCADE)

    class Meta:
        db_table = "ean"
        unique_together = (("item", "ean"),)


class ItemReplacement(models.Model):
    id = models.BigAutoField(primary_key=True)
    replacable = models.ForeignKey(
        BaseItem,
        models.CASCADE,
        db_column="replacable",
    )
    replacement = models.ForeignKey(
        BaseItem,
        models.CASCADE,
        db_column="replacement",
        related_name="itemreplacement_replacement_set",
    )

    class Meta:
        db_table = "item_replacement"
        unique_together = (("replacable", "replacement"),)


class MerchantItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=50)
    item = models.ForeignKey(Item, models.CASCADE)
    merchant = models.ForeignKey(Merchant, models.CASCADE)
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True
    )
    modified_at = models.DateTimeField(default=timezone.now())
    min_order = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = "merchant_item"
        unique_together = (("merchant", "item", "code", "min_order"),)


class MinLevel(models.Model):
    min_level_id = models.AutoField(primary_key=True)
    qty = models.IntegerField(default=1)
    branch = models.ForeignKey(Branch, models.CASCADE)
    merchant_item = models.ForeignKey(MerchantItem, models.CASCADE)
    modified_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "min_level"
        unique_together = (("merchant_item", "branch"),)


class ReturnItem(models.Model):
    item = models.ForeignKey(MerchantItem, models.CASCADE)
    return_item = models.ForeignKey(
        MerchantItem,
        models.SET_NULL,
        related_name="returnitem_return_item_set",
        blank=True,
        null=True,
    )
    id = models.BigAutoField(primary_key=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "return_item"
        unique_together = (("item", "return_item"),)
