from rest_framework import serializers

from journal.models import GroupStudent, Lesson
from people.models import Student


class LessonSerializer(serializers.ModelSerializer):
    """Сериалізатор дисциплін."""

    class Meta:
        model = Lesson
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):
    """Сериалізатор студентських груп."""
    grade = serializers.CharField()

    class Meta:
        model = GroupStudent
        fields = ['id', 'grade', 'create_group']


class GroupStudentSerializer(serializers.ModelSerializer):
    """Сериалізатор студентів в групах."""
    user_id = serializers.StringRelatedField(source='user.id')
    full_name = serializers.StringRelatedField(source='user.get_full_name')

    class Meta:
        model = Student
        fields = ['user_id', 'full_name']


class GroupDetailSerializer(serializers.ModelSerializer):
    """Сериалізатор даних групи."""
    lessons = LessonSerializer(source='grade.lessons', many=True)
    students = GroupStudentSerializer(many=True)
    grade = serializers.CharField()

    class Meta:
        model = GroupStudent
        fields = ['id', 'grade', 'create_group', 'lessons', 'students']