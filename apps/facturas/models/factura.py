from django.db import models

class Factura(models.Model):
    fecha_emision = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # llave secundaria nota venta
    notaventa_id = models.OneToOneField(
        'notaventas.NotaVenta',
        on_delete=models.CASCADE,
        related_name='facturas'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha_emision.strftime('%Y-%m-%d')
