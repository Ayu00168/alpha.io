from rest_framework import serializers
from .models import Product, ProductType
from drf_extra_fields.fields import Base64ImageField

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = [ "id", "name", "organisation" ]
        
        
class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = [ "id", "name", "price", "description", "image", "product_type", "quantity", "suffix", "organisation" ]