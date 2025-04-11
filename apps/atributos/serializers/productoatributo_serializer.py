from rest_framework import serializers
from apps.atributos.models import ProductoAtributo
from apps.products.serializers import ProductSerializer
from apps.atributos.serializers import AtributoSerializer

class ProductoAtributoSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    atributo = AtributoSerializer()

    class Meta:
        model = ProductoAtributo
        fields = ['product', 'atributo', 'valor']
