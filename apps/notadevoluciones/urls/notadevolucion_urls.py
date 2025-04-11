from django.urls import path
from apps.notadevoluciones.views import NotaDevolucionListCreateView, NotaDevolucionDetailView

urlpatterns = [
    path('', NotaDevolucionListCreateView.as_view(), name='notadevolucion-list-create'),
    path('<int:pk>/', NotaDevolucionDetailView.as_view(), name='notadevolucion-detail'),
]
