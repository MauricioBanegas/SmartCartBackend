from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.notadevoluciones.models.notadevolucion import NotaDevolucion
from apps.notadevoluciones.serializers.notadevolucion_serializer import NotaDevolucionSerializer

class NotaDevolucionListCreateView(generics.ListCreateAPIView):
    queryset = NotaDevolucion.objects.all().order_by('-created_at')
    serializer_class = NotaDevolucionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NotaDevolucionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotaDevolucion.objects.all()
    serializer_class = NotaDevolucionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]