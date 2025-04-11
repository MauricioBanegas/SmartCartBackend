from django.db import models

class NotaDevolucion(models.Model):
    fecha = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha.strftime("%Y-%m-%d")
