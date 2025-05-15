from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Siz faqat o'zingizga tegishli obyektlarni o'zgartira olasiz"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
