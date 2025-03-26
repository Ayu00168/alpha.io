from rest_framework import serializers
from .models import Order, Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    table = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'
        
    def get_table(self, obj):
        return {
            "id": obj.table.id,
            "name": obj.table.name,
            "capacity": obj.table.capacity
        }