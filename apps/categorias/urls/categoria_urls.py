from django.urls import path
from apps.categorias.views import CategoriaListCreateView, CategoriaDetailView

urlpatterns = [
    path('', CategoriaListCreateView.as_view(), name='categoria-list'),
    path('<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
]
