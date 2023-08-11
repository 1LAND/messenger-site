from rest_framework import permissions

class IsAuthenticatedOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) or bool(request.user and request.user.is_staff)