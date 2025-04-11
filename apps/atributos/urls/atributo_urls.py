from django.urls import path, include
from apps.atributos.views import AtributoListCreateView, AtributoDetailView

from rest_framework.routers import DefaultRouter
from apps.atributos.views import ProductoAtributoViewSet

router = DefaultRouter()
router.register(r'product-atributos', ProductoAtributoViewSet)

urlpatterns = [
    path('', AtributoListCreateView.as_view(), name='atributo-list-create'),
    path('<int:pk>/', AtributoDetailView.as_view(), name='atributo-detail'),
    
    path('api/', include(router.urls)),
]
