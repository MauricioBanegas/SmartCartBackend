from django.contrib import admin
from .models.metodopago import MetodoPago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'created_at')
    search_fields = ('tipo',)
