from django.contrib import admin
from .models.atributo import Atributo

@admin.register(Atributo)
class AtributoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'created_at')
    search_fields = ('nombre',)
