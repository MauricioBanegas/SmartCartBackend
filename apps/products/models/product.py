from django.db import models

class Product(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_min = models.PositiveIntegerField(default=2)
    imagen_url = models.TextField()
    estado = models.BooleanField(default=True)
    
    # llave secundaria categorias
    categoria_id = models.ForeignKey(
        'categorias.Categoria',
        on_delete=models.CASCADE,
        related_name='productos'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
