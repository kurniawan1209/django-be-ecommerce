from datetime import date
from django.contrib.auth.models import User
from django.db import models
from app_product.models import Products, ProductInventories

JOURNEY_TYPES = [
    ("WAITING_CONFIRMATION", "Waiting Confirmation By Seller"),
    ("CONFIRMED", "Order Confirmed By Seller"),
    ("PROCESSED", "Order Processed"),
    ("PICK_BY_SHIPPER", "Order Pick By Shipper"),
    ("ON_SHIPPING", "On The Way"),
    ("ORDER_SENDED", "Order Already Sended To Customer"),
    ("SUCCESS", "The order has been received well by the user"),
    ("FAILED", "The order is returned to seller")
]

class Wishlists(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key")
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name="Product Key")
    product_inv = models.ForeignKey(ProductInventories, on_delete=models.DO_NOTHING, verbose_name="Produt Detail Key", null=True)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "wishlists"

class Carts(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key")
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name="Product Key")
    product_inv = models.ForeignKey(ProductInventories, on_delete=models.DO_NOTHING, verbose_name="Produt Detail Key", null=True)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    wishlist = models.ForeignKey(Wishlists, on_delete=models.DO_NOTHING, verbose_name="Wishlist Key", null=True, blank=True, default=None)

    class Meta:
        db_table = "carts"
        

class TrxHeaders(models.Model):
    def auto_trx_number():
        try:
            data = TrxHeaders.objects.order_by("-creation_date").values("trx_number")[0]
            counter = str(int(data["trx_number"].replace("TRX", "")) + 1).zfill(9)
        except:
            counter = "1".zfill(9)
        return "TRX" + counter

    creation_date = models.DateTimeField(auto_now_add=True)
    trx_number = models.CharField(max_length=20, null=False, blank=False, default=auto_trx_number)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key")
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    city_id = models.IntegerField(default=0)
    city_name = models.CharField(max_length=100, default="")
    province_id = models.IntegerField(default=0)
    province_name = models.CharField(max_length=100, default="")
    country_name = models.CharField(max_length=100, default="indonesia")
    address = models.TextField()
    postal_code = models.CharField(max_length=10, default="")
    courier = models.CharField(max_length=10, default="")
    courier_service = models.CharField(max_length=20, default="")
    shipping_price = models.FloatField(default=0)
    estimation_date = models.DateField(default=date.today)

    class Meta:
        db_table = "trx_headers"


class TrxLines(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    header = models.ForeignKey(TrxHeaders, on_delete=models.DO_NOTHING, verbose_name="Transaction Header Key", related_name="trx_header_keys")
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name="Product Key")
    product_inv = models.ForeignKey(ProductInventories, on_delete=models.DO_NOTHING, verbose_name="Produt Detail Key", null=True)
    quantity = models.IntegerField()
    price = models.IntegerField(verbose_name="Price per piece", default=0, null=True, blank=True)
    cart = models.ForeignKey(Carts, on_delete=models.DO_NOTHING, verbose_name="Cart Key", default=None, blank=True, null=True)

    def auto_price(self):
        return self.product_inv.price
    
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.auto_price()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "trx_lines"


class TrxReviews(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    line = models.ForeignKey(TrxLines, on_delete=models.DO_NOTHING, verbose_name="Transaction Line Key")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key")
    review = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = "trx_reviews"


class TrxJourneys(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    header = models.ForeignKey(TrxHeaders, on_delete=models.DO_NOTHING, verbose_name="Transcation Header Key")
    journey_type = models.CharField(max_length=50, choices=JOURNEY_TYPES)
    estimation_date = models.DateField(default=None)
    description = models.TextField()

    class Meta:
        db_table = "trx_journeys"


class Payment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    payment_num = models.CharField(max_length=20, null=False, blank=False)
    header = models.ForeignKey(TrxHeaders, on_delete=models.DO_NOTHING, verbose_name="Transaction Header Key")
    amount = models.FloatField()
    payment_date = models.DateTimeField()
    expired_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = "payments"