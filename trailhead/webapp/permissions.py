from rest_framework import permissions

class IsTripLeader(permissions.BasePermission):
    """
    Custom permission to only allow trip leaders to access a view.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and if they are a trip leader
        return request.user.is_authenticated and request.user.student.is_trip_leader
