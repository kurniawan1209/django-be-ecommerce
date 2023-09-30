from django.contrib.auth.models import User
from django.db import models

AREA_TYPE = [
    ("CT", "City"),
    ("PV", "Province"),
    ("CN", "Country")
]

GENDERS = [
    ("f", "Female"),
    ("m", "Male"),
    ("u", "Unknown")
]

class UserDetails(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key", default=0, related_name="user_details_key")
    gender = models.CharField(max_length=10, choices=GENDERS, default="u")
    birth_date = models.DateField()

    class Meta:
        db_table = "user_details"

class UserAdresses(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key", default=0, related_name="user_address_key")
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    city_id = models.IntegerField(default=0)
    city_name = models.CharField(max_length=100, default="")
    province_id = models.IntegerField(default=0)
    province_name = models.CharField(max_length=100, default="")
    country_name = models.CharField(max_length=100, default="")
    address = models.TextField()
    tag = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "user_addresses"


class UserBalances(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="User Key")
    balance = models.IntegerField()

    class Meta:
        db_table = "user_balances"