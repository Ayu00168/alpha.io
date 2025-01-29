from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone']
        
        def create(self, validated_data):
            return User.objects.create(**validated_data)