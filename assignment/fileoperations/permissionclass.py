from rest_framework.permissions import BasePermission


class ClientUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_client
    



class OpsUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_ops