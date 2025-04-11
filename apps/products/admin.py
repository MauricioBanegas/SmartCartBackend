from django.contrib import admin
from .models.product import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion','stock_min',
                    'precio', 'imagen_url', 'estado','created_at')
    search_fields = ('nombre',)
