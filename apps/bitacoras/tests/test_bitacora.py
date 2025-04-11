from django.test import TestCase
from apps.bitacoras.models.bitacora import Bitacora

class BitacoraModelTest(TestCase):
    def test_create_bitacora(self):
        bitacora = Bitacora.objects.create(fecha='2023-10-01' )
        self.assertEqual(bitacora.fecha, '2023-10-01')
