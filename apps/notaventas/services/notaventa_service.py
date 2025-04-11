from datetime import datetime
from typing import List, Optional
from apps.notaventas.models import NotaVenta
from apps.notaventas.serializers import NotaVentaSerializer
from django.db import transaction

class NotaVentaService:
    @staticmethod
    def create_nota_venta(data: dict) -> NotaVenta:
        """
        Creates a new NotaVenta instance.
        """
        serializer = NotaVentaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            nota_venta = serializer.save()
        return nota_venta

    @staticmethod
    def get_nota_venta_by_id(nota_venta_id: int) -> Optional[NotaVenta]:
        """
        Retrieves a NotaVenta instance by its ID.
        """
        try:
            return NotaVenta.objects.get(id=nota_venta_id)
        except NotaVenta.DoesNotExist:
            return None

    @staticmethod
    def list_notas_venta() -> List[NotaVenta]:
        """
        Retrieves all NotaVenta instances.
        """
        return NotaVenta.objects.all()

    @staticmethod
    def update_nota_venta(nota_venta_id: int, data: dict) -> Optional[NotaVenta]:
        """
        Updates an existing NotaVenta instance.
        """
        nota_venta = NotaVentaService.get_nota_venta_by_id(nota_venta_id)
        if not nota_venta:
            return None
        serializer = NotaVentaSerializer(nota_venta, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            nota_venta = serializer.save()
        return nota_venta

    @staticmethod
    def delete_nota_venta(nota_venta_id: int) -> bool:
        """
        Deletes a NotaVenta instance by its ID.
        """
        nota_venta = NotaVentaService.get_nota_venta_by_id(nota_venta_id)
        if not nota_venta:
            return False
        with transaction.atomic():
            nota_venta.delete()
        return True