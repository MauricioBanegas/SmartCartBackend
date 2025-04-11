from django.contrib import admin
from .models.notadevolucion import NotaDevolucion

@admin.register(NotaDevolucion)
class NotaDevolucionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'created_at')
    search_fields = ('fecha',)
