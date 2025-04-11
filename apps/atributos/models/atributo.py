from django.db import models

class Atributo(models.Model):
    nombre = models.CharField(max_length=255)
    
    productos = models.ManyToManyField(
        'products.Product',
        through='ProductoAtributo',
        related_name='atributos',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

