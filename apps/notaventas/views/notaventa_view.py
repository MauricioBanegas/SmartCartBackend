from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.notaventas.models.notaventa import NotaVenta
from apps.notaventas.serializers.notaventa_serializer import NotaVentaSerializer

class NotaVentaListCreateView(generics.ListCreateAPIView):
    queryset = NotaVenta.objects.all().order_by('-created_at')
    serializer_class = NotaVentaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NotaVentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaVenta.objects.all()
    serializer_class =NotaVentaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]