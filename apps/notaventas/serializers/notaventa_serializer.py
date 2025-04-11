from rest_framework import serializers
from apps.notaventas.models.notaventa import NotaVenta

class NotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaVenta
        fields = '__all__'
