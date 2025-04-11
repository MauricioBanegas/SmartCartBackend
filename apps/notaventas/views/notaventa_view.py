from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.notaventas.models.detalleventa import DetalleVenta
from apps.notaventas.models.notaventa import NotaVenta
from apps.notaventas.serializers.detalleventa_serializer import DetalleVentaSerializer
from apps.notaventas.serializers.notaventa_serializer import NotaVentaSerializer


from rest_framework import viewsets
from rest_framework.decorators import action
class NotaVentaListCreateView(generics.ListCreateAPIView):
    queryset = NotaVenta.objects.all().order_by('-created_at')
    serializer_class = NotaVentaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NotaVentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaVenta.objects.all()
    serializer_class =NotaVentaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer