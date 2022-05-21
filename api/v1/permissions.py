from rest_framework import permissions
from rest_framework.permissions import BasePermission

from django_journal.settings import TEACHER
from journal.models import Lesson
from people.models import Teacher


class IsTeacher(BasePermission):
    """Тільки викладач"""
    def has_permission(self, request, view):
        return request.user.user_status == TEACHER


class IsTeacherOrOwnerUser(BasePermission):
    """
    Викладач або користувач-власник.
    GET(перегляд) - всы викладачы або користувач-власник.
    Ыншы методы (UPDATE) - тільки викладачі.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and \
                (request.user.user_status == TEACHER or obj.id == request.user.id):
            return True
        return request.user.user_status == TEACHER


class IsOwnerUser(BasePermission):
    """Тільки той викладач, що створив оцінку."""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.teacher


class IsTeacherLesson(BasePermission):
    """Викладач, який веде дисципліну."""
    def has_permission(self, request, view):
        teacher = Teacher.objects.prefetch_related('lessons') \
            .filter(user=request.user, lessons=view.kwargs.get('lesson_id', None)).exists()
        lesson_in_group = Lesson.objects\
            .filter(grade__group=view.kwargs.get('group_id', None), id=view.kwargs.get('lesson_id', None))
        return request.user.user_status == TEACHER and teacher and lesson_in_group
