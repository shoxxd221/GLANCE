from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuserOrStaffOrReadOnly(BasePermission):
    """
    Класс прав доступа чтение - любому пользователю, а создание, удаление и редактирование только
    суперпользователю или администратору.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user.is_superuser or request.user.is_staff
        )
