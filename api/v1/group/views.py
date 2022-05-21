from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.v1.group.serializers import GroupSerializer, GroupDetailSerializer
from api.v1.permissions import IsTeacher
from journal.models import GroupStudent


class GroupListView(generics.ListAPIView):
    """Виведення усіх студентських груп."""
    queryset = GroupStudent.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsTeacher)


class GroupDetailView(generics.RetrieveAPIView):
    """Виведення інформації про групу."""
    queryset = GroupStudent.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = (IsAuthenticated, IsTeacher)
