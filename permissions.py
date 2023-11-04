from rest_framework.permissions import BasePermission

from user.models import ITAdmin

class IsITAdmin(BasePermission):
    message = "Permission Denied. You're Not an IT Admin"

    def has_permission(self, request, view):
        user = request.user.is_authenticated and request.user.role == "ADM"
        is_itadmin = ITAdmin.objects.filter(user = request.user).exists()
        return user and is_itadmin