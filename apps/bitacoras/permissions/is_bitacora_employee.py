from rest_framework.permissions import BasePermission

class IsBitacoraEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'EMPLEADO'
