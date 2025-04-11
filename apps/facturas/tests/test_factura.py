from django.test import TestCase
from apps.facturas.models.factura import Factura

class FacturaModelTest(TestCase):
    def test_create_factura(self):
        factura = Factura.objects.create(fecha_emision='2023-10-01', total=100.00)
        self.assertEqual(factura.fecha_emision, '2023-10-01')
