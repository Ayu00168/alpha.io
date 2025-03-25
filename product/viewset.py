from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, ProductType
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer, ProductTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
    
    
    
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer