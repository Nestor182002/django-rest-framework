from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserToUser(BasePermission):
    message = "only for the user himself"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.client_id.id == request.user.id



        