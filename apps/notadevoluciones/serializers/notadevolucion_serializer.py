from rest_framework import serializers
from apps.notadevoluciones.models.notadevolucion import NotaDevolucion

class NotaDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaDevolucion
        fields = '__all__'
