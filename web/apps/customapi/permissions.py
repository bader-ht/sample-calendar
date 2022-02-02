from rest_framework.permissions import IsAuthenticated

class IsMyAccount(IsAuthenticated):
    """
    Permission to verify that only the owner can see his account details.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

