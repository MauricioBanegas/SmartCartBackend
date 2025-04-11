from django.db import models 

# relación de muchos a muchos con productos usando una tabla intermedia
class DetalleVenta(models.Model):
    notaventa = models.ForeignKey('NotaVenta', on_delete=models.CASCADE)
    producto = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('notaventa', 'producto')
        
    def __str__(self):
        return f'{self.notaventa.fecha} - {self.producto.nombre}: {self.cantidad} - {self.precio_unitario}'
