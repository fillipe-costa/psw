from rest_framework import permissions

#Aqui só permitiremos que o usúario veja detalhes de seus próprios pedidos
class IsOrderOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, order_obj):
        return order_obj.user.id == request.user.id
