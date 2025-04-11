from typing import Optional
from apps.descuentos.models import Descuento
from django.core.exceptions import ObjectDoesNotExist

class DescuentoService:
    @staticmethod
    def obtener_descuento_por_id(descuento_id: int) -> Optional[Descuento]:
        """
        Obtiene un descuento por su ID.
        """
        try:
            return Descuento.objects.get(id=descuento_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_descuento(nombre: str, porcentaje: float, activo: bool) -> Descuento:
        """
        Crea un nuevo descuento.
        """
        descuento = Descuento(nombre=nombre, porcentaje=porcentaje, activo=activo)
        descuento.save()
        return descuento

    @staticmethod
    def actualizar_descuento(descuento_id: int, nombre: Optional[str] = None, porcentaje: Optional[float] = None, activo: Optional[bool] = None) -> Optional[Descuento]:
        """
        Actualiza un descuento existente.
        """
        descuento = DescuentoService.obtener_descuento_por_id(descuento_id)
        if not descuento:
            return None

        if nombre is not None:
            descuento.nombre = nombre
        if porcentaje is not None:
            descuento.porcentaje = porcentaje
        if activo is not None:
            descuento.activo = activo

        descuento.save()
        return descuento

    @staticmethod
    def eliminar_descuento(descuento_id: int) -> bool:
        """
        Elimina un descuento por su ID.
        """
        descuento = DescuentoService.obtener_descuento_por_id(descuento_id)
        if not descuento:
            return False

        descuento.delete()
        return True

    @staticmethod
    def listar_descuentos(activo: Optional[bool] = None) -> list[Descuento]:
        """
        Lista todos los descuentos, opcionalmente filtrados por estado activo.
        """
        if activo is not None:
            return list(Descuento.objects.filter(activo=activo))
        return list(Descuento.objects.all())