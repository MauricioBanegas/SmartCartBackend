from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.metodopagos.models.metodopago import MetodoPago
from apps.metodopagos.serializers.metodopago_serializer import MetodoPagoSerializer

class MetodoPagoListCreateView(generics.ListCreateAPIView):
    queryset = MetodoPago.objects.all().order_by('-created_at')
    serializer_class = MetodoPagoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MetodoPagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]