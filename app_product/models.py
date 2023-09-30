from django.db import models

class Brands(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.FileField(null=True, blank=True)

    class Meta:
        db_table = "brands"


class ProductCategories(models.Model):
    creation_date = models.DateTimeField(auto_now_add=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.FileField(upload_to="../img/product-categories/", null=True, blank=True)

    class Meta:
        db_table = "product_categories"


class Products(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, null=False, blank=False, unique=True, default="default")
    name = models.CharField(max_length=225, null=False, blank=False)
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name="Brand Key")
    category = models.ForeignKey(ProductCategories, on_delete=models.DO_NOTHING, verbose_name="Category Key")
    description = models.TextField()

    class Meta:
        db_table = "products"


class ProductDetails(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name="Product Key", related_name="detail_product_keys")
    key = models.CharField(max_length=50, null=False, blank=False)
    value = models.TextField(null=False, blank=False)

    class Meta:
        db_table = "product_details"


class ProductInventories(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name="Product Key", related_name="inv_product_keys")
    size = models.IntegerField()
    color = models.CharField(max_length=15)
    stock = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = "product_inventories"