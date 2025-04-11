from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.atributos.models.atributo import Atributo
from apps.atributos.serializers.atributo_serializer import AtributoSerializer

from rest_framework import viewsets
from apps.atributos.models import ProductoAtributo
from apps.atributos.serializers import ProductoAtributoSerializer
from rest_framework.decorators import action

class AtributoListCreateView(generics.ListCreateAPIView):
    queryset = Atributo.objects.all().order_by('-created_at')
    serializer_class = AtributoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AtributoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atributo.objects.all()
    serializer_class = AtributoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ProductoAtributoViewSet(viewsets.ModelViewSet):
    queryset = ProductoAtributo.objects.all()
    serializer_class = ProductoAtributoSerializer