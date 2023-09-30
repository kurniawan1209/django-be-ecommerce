from rest_framework import serializers
from .models import Brands, ProductCategories, ProductDetails, ProductInventories, Products

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventories
        fields = "__all__"

class PrimaryProductSerializer(serializers.ModelSerializer):
    details = ProductDetailSerializer(many=True, source="detail_product_keys")
    inventory = ProductInventorySerializer(many=True, source="inv_product_keys")
    image = serializers.CharField()
    total_stock = serializers.IntegerField()
    price = serializers.FloatField()
    brand_name = serializers.CharField()
    category_name = serializers.CharField()

    class Meta:
        model = Products
        fields = "__all__"

class SecondayProductSerializer(serializers.ModelSerializer):
    image = serializers.CharField()
    total_stock = serializers.IntegerField()
    price = serializers.FloatField()
    brand_name = serializers.CharField()
    category_name = serializers.CharField()

    class Meta:
        model = Products
        fields = "__all__"