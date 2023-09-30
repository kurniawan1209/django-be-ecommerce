from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserAdresses, UserBalances, UserDetails

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdresses
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer(many=True, source="user_address_key")
    class Meta:
        model = get_user_model()
        fields = "__all__"
        
class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalances
        fields = "__all__"

class UserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"