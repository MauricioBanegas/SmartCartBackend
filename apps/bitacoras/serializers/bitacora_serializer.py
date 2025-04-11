from rest_framework import serializers
from apps.bitacoras.models.bitacora import Bitacora

class BitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitacora
        fields = '__all__'
