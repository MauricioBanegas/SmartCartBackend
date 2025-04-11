from django.db import models 

# relación de muchos a muchos con productos usando una tabla intermedia
class ProductoAtributo(models.Model):
    atributo = models.ForeignKey('Atributo', on_delete=models.CASCADE)
    producto = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)  # atributo adicional en la tabla intermedia

    class Meta:
        unique_together = ('atributo', 'producto')
        
    def __str__(self):
        return f'{self.atributo.nombre} - {self.product.nombre}: {self.valor}'
