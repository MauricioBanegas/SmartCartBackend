from django.test import TestCase
from apps.notadevoluciones.models.notadevolucion import NotaDevolucion

class NotaDevolucionModelTest(TestCase):
    def test_create_notadevolucion(self):
        notadevolucion = NotaDevolucion.objects.create(fecha='Test')
        self.assertEqual(notadevolucion.fecha, 'Test')
