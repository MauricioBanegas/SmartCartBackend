from django.test import TestCase
from apps.atributos.models.atributo import Atributo

class AtributoModelTest(TestCase):
    def test_create_categoria(self):
        atributo = Atributo.objects.create(nombre='Test')
        self.assertEqual(atributo.nombre, 'Test')
