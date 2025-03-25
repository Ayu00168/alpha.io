from rest_framework import serializers
from .models import Order, Tables


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = '__all__'