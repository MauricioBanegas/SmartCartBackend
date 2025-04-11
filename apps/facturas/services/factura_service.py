from apps.facturas.models import Factura
from apps.facturas.serializers import FacturaSerializer
from rest_framework.exceptions import NotFound

class FacturaService:
    @staticmethod
    def get_factura_by_id(factura_id):
        try:
            return Factura.objects.get(id=factura_id)
        except Factura.DoesNotExist:
            raise NotFound(detail="Factura not found.")

    @staticmethod
    def create_factura(data):
        serializer = FacturaSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    @staticmethod
    def update_factura(factura_id, data):
        factura = FacturaService.get_factura_by_id(factura_id)
        serializer = FacturaSerializer(factura, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    @staticmethod
    def delete_factura(factura_id):
        factura = FacturaService.get_factura_by_id(factura_id)
        factura.delete()
        return {"detail": "Factura deleted successfully."}

    @staticmethod
    def list_facturas():
        return Factura.objects.all()