from rest_framework.permissions import BasePermission

class IsMetodoPagoEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'EMPLEADO'
