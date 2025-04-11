from django.test import TestCase
from apps.metodopagos.models.metodopago import MetodoPago

class MetodoPagoModelTest(TestCase):
    def test_create_product(self):
        metodopago = MetodoPago.objects.create(tipo='Test')
        self.assertEqual(metodopago.tipo, 'Test')
