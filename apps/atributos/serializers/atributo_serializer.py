from rest_framework import serializers
from apps.atributos.models.atributo import Atributo

class AtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atributo
        fields = '__all__'