from django.urls import path
from apps.bitacoras.views import BitacoraListCreateView, BitacoraDetailView

urlpatterns = [
    path('', BitacoraListCreateView.as_view(), name='bitacora-list'),
    path('<int:pk>/', BitacoraDetailView.as_view(), name='bitacora-detail'),
]
