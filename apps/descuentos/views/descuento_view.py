from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.descuentos.models.descuento import Descuento
from apps.descuentos.serializers.descuento_serializer import DescuentoSerializer

class DescuentoListCreateView(generics.ListCreateAPIView):
    queryset = Descuento.objects.all().order_by('-created_at')
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DescuentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]