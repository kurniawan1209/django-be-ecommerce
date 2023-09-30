from rest_framework import serializers
from .models import Carts, TrxHeaders, TrxJourneys, TrxLines, TrxReviews, Wishlists

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = "__all__"

class TrxLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrxLines
        fields = "__all__"

class TrxHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrxHeaders
        fields = "__all__"

class TransactionListSerializer(serializers.ModelSerializer):
    lines = TrxLineSerializer(many=True, source="trx_header_keys")
    class Meta:
        model = TrxHeaders
        fields = "__all__"

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = "__all__"