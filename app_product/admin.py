from django.contrib import admin
from .models import Brands, ProductCategories, ProductDetails, Products

admin.site.register([Brands, ProductCategories, ProductDetails, Products])
