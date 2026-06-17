from rest_framework import permissions


class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return request.user.role.name=='student'
    


class IsFaculty(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return request.user.role.name=='faculty'