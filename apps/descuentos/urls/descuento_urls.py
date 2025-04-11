from django.urls import path
from apps.descuentos.views import DescuentoListCreateView, DescuentoDetailView

urlpatterns = [
    path('', DescuentoListCreateView.as_view(), name='descuento-list-create'),
    path('<int:pk>/', DescuentoDetailView.as_view(), name='descuento-detail'),
]
