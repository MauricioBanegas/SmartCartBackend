from django.urls import path
from apps.notaventas.views import NotaVentaListCreateView, NotaVentaDetailView

urlpatterns = [
    path('', NotaVentaListCreateView.as_view(), name='notaventa-list-create'),
    path('<int:pk>/', NotaVentaDetailView.as_view(), name='notaventa-detail'),
]
