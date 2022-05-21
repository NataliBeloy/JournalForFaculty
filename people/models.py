from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse_lazy

from django_journal.settings import USER_STATUS_CHOICES, GENDER_CHOICES, STUDY_CHOICES, STUDY_DEGREE_CHOICES, TEACHER


class User(AbstractUser):
    """Користувач."""
    first_name = models.CharField('Ім\'я', max_length=130)
    last_name  = models.CharField('Фамілія', max_length=130)
    middle_name = models.CharField('По-батькові', max_length=130)
    sex = models.CharField('Стать', choices=GENDER_CHOICES, max_length=1)
    birth_date = models.DateField('Дата народження', blank=True, null=True)
    photo = models.ImageField(upload_to='people/', default='static/img/default-user.png', blank=True)
    description = models.TextField('Характеристика')
    user_status = models.CharField('Статус користувача', choices=USER_STATUS_CHOICES, max_length=15)
    updated = models.DateField('Дата оновлення', auto_now=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.last_name+" "+self.first_name+" "+self.middle_name

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'


class Contact(models.Model):
    """Контактні дані студентів, викладачів"""
    phone1 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 1')
    phone2 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 2')
    phone3 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 3')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='contact', null=True, blank=True,
                                verbose_name='Контактные данные', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone1

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'


class Teacher(models.Model):
    """Викладачі"""
    position = models.CharField('Посада', max_length=99)
    group_manager = models.ForeignKey('journal.GroupStudent', related_name='teacher',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    lessons = models.ManyToManyField('journal.Lesson', related_name='teachers', verbose_name='Викладає дисципліни')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('teacher_detail', kwargs={'pk': self.user_id})

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'


class Student(models.Model):
    """Студенти"""
    study_form = models.CharField('Форма навчання', choices=STUDY_CHOICES, max_length=20)
    study_degree = models.CharField('Ступінь навчання', choices=STUDY_DEGREE_CHOICES, max_length=30)
    entry_year = models.IntegerField('Рік вступу')
    group = models.ForeignKey('journal.GroupStudent', related_name='students', verbose_name='Навчається в групі',
                              on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE)
    course_work = models.CharField('Тема курсової роботи', max_length=100)
    course_supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='supervisor', on_delete=models.SET_NULL,
                                null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Викладач')
    diploma_work = models.CharField('Тема курсової роботи', max_length=100)
    diploma_supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='supervisors',
                                          on_delete=models.SET_NULL,
                                          null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Викладач')


    def get_absolute_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.user_id})

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'
