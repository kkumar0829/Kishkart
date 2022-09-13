from rest_framework import serializers
from .models import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartData
        fields = '__all__'


# class PriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductPrice
#         fields = '__all__'
