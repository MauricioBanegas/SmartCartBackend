from django.db import models

class Bitacora(models.Model):
    fecha = models.DateField()
    accion = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    
    # llave secundaria usuario
    usuario_id = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bitacoras'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha.strftime('%Y-%m-%d')
