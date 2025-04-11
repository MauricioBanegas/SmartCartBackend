from django.test import TestCase
from apps.descuentos.models.descuento import Descuento

class DescuentoModelTest(TestCase):
    def test_create_descuento(self):
        descuento = Descuento.objects.create(name='Test', porcentaje=10.0, accion='Test Action', porcentaje_descuento=5.0)
        self.assertEqual(descuento.name, 'Test')
