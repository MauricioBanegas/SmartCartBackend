from apps.metodopagos.models import MetodoPago
from apps.metodopagos.serializers import MetodoPagoSerializer
from rest_framework.exceptions import NotFound

class MetodoPagoService:
    @staticmethod
    def obtener_metodo_pago_por_id(metodo_pago_id):
        try:
            return MetodoPago.objects.get(id=metodo_pago_id)
        except MetodoPago.DoesNotExist:
            raise NotFound(f"Método de pago con ID {metodo_pago_id} no encontrado.")

    @staticmethod
    def listar_metodos_pago():
        return MetodoPago.objects.all()

    @staticmethod
    def crear_metodo_pago(datos):
        serializer = MetodoPagoSerializer(data=datos)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    @staticmethod
    def actualizar_metodo_pago(metodo_pago_id, datos):
        metodo_pago = MetodoPagoService.obtener_metodo_pago_por_id(metodo_pago_id)
        serializer = MetodoPagoSerializer(metodo_pago, data=datos, partial=True)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    @staticmethod
    def eliminar_metodo_pago(metodo_pago_id):
        metodo_pago = MetodoPagoService.obtener_metodo_pago_por_id(metodo_pago_id)
        metodo_pago.delete()