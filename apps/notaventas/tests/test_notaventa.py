from django.test import TestCase
from apps.notaventas.models import notaventa
from apps.notaventas.models.notaventa import NotaVenta

class NotaVentaModelTest(TestCase):
    def test_create_notaventa(self):
        product = NotaVenta.objects.create(fecha='2023-10-01')
        self.assertEqual(notaventa.fecha, '2023-10-01')
