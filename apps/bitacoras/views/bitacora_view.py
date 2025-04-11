from rest_framework import generics
from apps.bitacoras.models import Bitacora
from apps.bitacoras.serializers import BitacoraSerializer

class BitacoraListCreateView(generics.ListCreateAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer

class BitacoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Bitacora.objects.all()
    serializer_class =BitacoraSerializer
