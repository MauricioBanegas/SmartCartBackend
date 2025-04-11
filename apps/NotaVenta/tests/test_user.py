from django.test import TestCase
from apps.products.models.product import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name='Test', price=9.99, stock=10, category='General')
        self.assertEqual(product.name, 'Test')
