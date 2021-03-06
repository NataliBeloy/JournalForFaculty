from rest_framework import serializers
from rest_framework.authtoken.models import Token

from journal.models import Lesson
from people.models import User, Teacher, Contact, Student


class UserSerializer(serializers.ModelSerializer):
    """Сериалізатор користувача."""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'birth_date', 'sex', 'photo', 'user_status']


class LessonSerializer(serializers.ModelSerializer):
    """Сериалізатор дисциплін."""
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'grade']


class ContactSerializer(serializers.ModelSerializer):
    """Сериалізатор контактних даних."""
    class Meta:
        model = Contact
        fields = ['phone1', 'phone2', 'phone3']


class TeacherSerializer(serializers.ModelSerializer):
    """Сериалізатор даних викладача."""
    lessons = LessonSerializer(many=True)
    group_manager = serializers.CharField()

    class Meta:
        model = Teacher
        fields = ['position', 'group_manager', 'lessons']


class UserTeacherDetailSerializer(serializers.ModelSerializer):
    """Сериалізатор користувача-викладача."""
    contact = ContactSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'birth_date', 'sex', 'description', 'photo',
                  'user_status', 'contact', 'teacher']


class StudentSerializer(serializers.ModelSerializer):
    """Сериалізатор студента."""
    class Meta:
        model = Student
        fields = ['group', 'study_form']


class UserStudentDetailSerializer(serializers.ModelSerializer):
    """Сериалізатор перегляду і оновлення даних користувача-студента."""
    contact = ContactSerializer()
    group = StudentSerializer(source='student')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'birth_date', 'sex',
                  'description', 'photo', 'user_status', 'contact', 'group']

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact')
        contact = instance.contact
        contact_serializer = self.fields['contact']
        contact_serializer.update(contact, contact_data)

        group_data = validated_data.pop('student')
        group = instance.student
        group_serializer = self.fields['group']
        group_serializer.update(group, group_data)

        validated_data['user_status'] = 'student'
        return super(UserStudentDetailSerializer, self).update(instance, validated_data)


class UserStudentCreateSerializer(serializers.ModelSerializer):
    """Сериалізатор для створення студента."""
    contact = ContactSerializer()
    group = StudentSerializer(source='student')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'middle_name',
                  'birth_date', 'sex', 'description', 'photo', 'user_status', 'contact', 'group', 'study_form']

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        group = validated_data.pop('student')

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.user_status = 'student'
        user.save()

        Contact.objects.create(user=user, **contact_data)
        Student.objects.create(user=user, group=group['group'])
        Token.objects.create(user=user)
        return user
