from .serializer import OrderSerializer, TableSerializer
from rest_framework import viewsets
from .models import Order, Table
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        organisation = user.organisation
        table_id = self.request.query_params.get('table_id', None)
        
        if table_id:
            return Order.objects.filter(table_id=table_id, organisation=organisation)
        return Order.objects.filter(organisation=organisation)
    
    
class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Table.objects.filter(organisation=self.request.user.organisation)