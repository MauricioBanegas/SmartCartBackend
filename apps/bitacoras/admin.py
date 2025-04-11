from django.contrib import admin
from .models.bitacora import Bitacora

@admin.register(Bitacora)
class BitacoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha','accion', 'ip', 'created_at')
    search_fields = ('fecha',)
