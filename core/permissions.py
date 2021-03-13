from rest_framework import permissions

class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """
    message = 'You must be the owner of this object.'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.user == request.user: 
            return True
        else:
            return False