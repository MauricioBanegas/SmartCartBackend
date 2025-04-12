from django.urls import include, path
from apps.notaventas.views import NotaVentaListCreateView, NotaVentaDetailView

from rest_framework.routers import DefaultRouter
from apps.notaventas.views import DetalleVentaViewSet

router = DefaultRouter()
router.register(r'detalle-ventas', DetalleVentaViewSet)

urlpatterns = [
    path('', NotaVentaListCreateView.as_view(), name='notaventa-list-create'),
    path('<int:pk>/', NotaVentaDetailView.as_view(), name='notaventa-detail'),
    
    path('api/', include(router.urls)),
]
