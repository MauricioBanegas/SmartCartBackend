from rest_framework import serializers
from apps.notaventas.models.detalleventa import DetalleVenta
from apps.products.serializers import ProductSerializer
from apps.notaventas.serializers import NotaVentaSerializer

class DetalleVentaSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    atributo = NotaVentaSerializer()

    class Meta:
        model = DetalleVenta
        fields = ['product', 'notaventa', 'cantidad', 'precio_unitario']
