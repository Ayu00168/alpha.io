from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(required=False)
    class Meta:
        model = Organisation
        fields = [ "id", "name", "email", "phone", "address", "city", "state", "country", "pincode", "is_active", "logo" ]