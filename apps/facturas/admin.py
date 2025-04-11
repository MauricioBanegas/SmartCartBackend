from django.contrib import admin
from .models.factura import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_emision','total', 'created_at')
    search_fields = ('fecha_emision',)
