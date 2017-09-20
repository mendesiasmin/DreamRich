from rest_framework import permissions
import rolepermissions

class SomePermission(permissions.BasePermission):
    message = 'My custom permission'

    def has_permission(self, request, view):
        user = request.user
        permissions = rolepermissions.permissions.available_perm_status(user)
        print(view.required_permission, permissions)
        if view.required_permission in permissions:
            a = permissions[view.required_permission]
            print(a)
            return a
        return False


