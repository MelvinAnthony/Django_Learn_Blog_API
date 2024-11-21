from rest_framework import permissions


class IsAdminUserorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True        
        else:
            return request.user and request.user.is_staff
        

class IsOwnerorReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        else:
            print("this is obj: ",obj)
            return obj.author == request.user
        