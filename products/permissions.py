from rest_framework import permissions

#Aqui só permitiremos que o usúario crie, altere ou delete produtos se for administrador
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or (request.user and request.user.is_staff):
            return True
        else:
            return False
