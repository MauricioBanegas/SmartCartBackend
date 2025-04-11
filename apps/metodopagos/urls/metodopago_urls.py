from django.urls import path
from apps.metodopagos.views import MetodoPagoListCreateView, MetodoPagoDetailView

urlpatterns = [
    path('', MetodoPagoListCreateView.as_view(), name='metodopago-list-create'),
    path('<int:pk>/', MetodoPagoDetailView.as_view(), name='metodopago-detail'),
]
