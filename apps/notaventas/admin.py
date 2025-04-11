from django.contrib import admin
from .models.notaventa import NotaVenta

@admin.register(NotaVenta)
class NotaVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha',  'created_at')
    search_fields = ('fecha',)
