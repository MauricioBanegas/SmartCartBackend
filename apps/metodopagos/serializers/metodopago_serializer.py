from rest_framework import serializers
from apps.metodopagos.models.metodopago import MetodoPago

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'
