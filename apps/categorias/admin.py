from django.contrib import admin
from .models.categoria import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'created_at')
    search_fields = ('nombre',)
