from apps.notadevoluciones.models import NotaDevolucion
from apps.notadevoluciones.serializers import NotaDevolucionSerializer
from rest_framework.exceptions import NotFound

class NotaDevolucionService:
    @staticmethod
    def create_nota_devolucion(data):
        """
        Create a new NotaDevolucion instance.
        """
        serializer = NotaDevolucionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @staticmethod
    def get_nota_devolucion_by_id(nota_devolucion_id):
        """
        Retrieve a NotaDevolucion by its ID.
        """
        try:
            return NotaDevolucion.objects.get(id=nota_devolucion_id)
        except NotaDevolucion.DoesNotExist:
            raise NotFound(f"NotaDevolucion with ID {nota_devolucion_id} not found.")

    @staticmethod
    def update_nota_devolucion(nota_devolucion_id, data):
        """
        Update an existing NotaDevolucion instance.
        """
        nota_devolucion = NotaDevolucionService.get_nota_devolucion_by_id(nota_devolucion_id)
        serializer = NotaDevolucionSerializer(nota_devolucion, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @staticmethod
    def delete_nota_devolucion(nota_devolucion_id):
        """
        Delete a NotaDevolucion instance.
        """
        nota_devolucion = NotaDevolucionService.get_nota_devolucion_by_id(nota_devolucion_id)
        nota_devolucion.delete()
        return {"message": f"NotaDevolucion with ID {nota_devolucion_id} has been deleted."}