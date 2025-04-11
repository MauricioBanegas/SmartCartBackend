from django.test import TestCase
from apps.products.models.product import Product


# falta acomodar con todos los campos del producto para los test
class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(nombre='Test', descripcion='algo',precio=9.99, stock_min=10, imagen_url='por/ahi/se/busca', estado=True)
        self.assertEqual(product.nombre, 'Test')
