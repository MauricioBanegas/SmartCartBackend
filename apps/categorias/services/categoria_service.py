from apps.categorias.models import Categoria
from django.core.exceptions import ObjectDoesNotExist

class CategoriaService:
    @staticmethod
    def crear_categoria(nombre, descripcion):
        """Crea una nueva categoría."""
        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        categoria.save()
        return categoria

    @staticmethod
    def obtener_categoria_por_id(categoria_id):
        """Obtiene una categoría por su ID."""
        try:
            return Categoria.objects.get(id=categoria_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def listar_categorias():
        """Lista todas las categorías."""
        return Categoria.objects.all()

    @staticmethod
    def actualizar_categoria(categoria_id, nombre=None, descripcion=None):
        """Actualiza los datos de una categoría existente."""
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            if nombre:
                categoria.nombre = nombre
            if descripcion:
                categoria.descripcion = descripcion
            categoria.save()
            return categoria
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def eliminar_categoria(categoria_id):
        """Elimina una categoría por su ID."""
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            categoria.delete()
            return True
        except ObjectDoesNotExist:
            return False