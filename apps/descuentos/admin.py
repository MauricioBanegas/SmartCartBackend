from django.contrib import admin
from .models.descuento import Descuento

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'porcentaje', 'created_at')
    search_fields = ('nombre',)
