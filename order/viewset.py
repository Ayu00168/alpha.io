from rest_framework import viewsets
from .serializers import OrderSerializer, TablesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Order, Tables

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        queryset  = Order.objects.all()
        return queryset
    
    
    
    
class TablesViewSet(viewsets.ModelViewSet):
    serializer_class = TablesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        queryset  = Tables.objects.all()
        return queryset