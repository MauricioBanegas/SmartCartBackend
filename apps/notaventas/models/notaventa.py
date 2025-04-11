from django.db import models

class NotaVenta(models.Model):
    fecha = models.DateField()
    
    # relacion de one a uno con factura
    # la nota de venta tiene una factura y la factura tiene una nota de venta
    # factura = models.OneToOneField(
    #     'Factura',
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True
    # )
    # # usuario que realiza la conpra seria el cliente con el rol cliente
    # usuario = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='notas_venta')
    # # usuario que realiza la venta seria el vendedor con el rol vendedor
    # vendedor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='ventas_realizadas')
    # # cliente que realiza la compra seria el cliente con el rol cliente
    # cliente = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='compras_realizadas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha
