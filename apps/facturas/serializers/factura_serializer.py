from rest_framework import serializers
from apps.facturas.models.factura import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
