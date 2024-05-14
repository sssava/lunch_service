from rest_framework import permissions


class IsRestaurantOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "Restaurant"

    def has_permission(self, request, view):
        return request.user.role == "Restaurant"
