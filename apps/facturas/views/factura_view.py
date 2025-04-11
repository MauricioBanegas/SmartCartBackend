from rest_framework import generics
from apps.facturas.models import Factura
from apps.facturas.serializers import FacturaSerializer

class FacturaListCreateView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
