from django.urls import path
from apps.facturas.views import FacturaListCreateView, FacturaDetailView

urlpatterns = [
    path('', FacturaListCreateView.as_view(), name='factura-list'),
    path('<int:pk>/', FacturaDetailView.as_view(), name='factura-detail'),
]
