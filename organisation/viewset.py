from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organisation
from .serializers import OrganisationSerializer
from rest_framework.authentication import TokenAuthentication

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


