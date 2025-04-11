from rest_framework import serializers
from apps.descuentos.models.descuento import Descuento

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'
