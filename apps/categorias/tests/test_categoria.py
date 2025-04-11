from django.test import TestCase
from apps.categorias.models.categoria import Categoria

class CategoriaModelTest(TestCase):
    def test_create_categoria(self):
        categoria = Categoria.objects.create(name='Test', descripcion='ingreso algo')
        self.assertEqual(categoria.name, 'Test')
