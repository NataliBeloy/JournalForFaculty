from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django_journal.settings import SCORE_CHOICES, STUDENT, TEACHER
from people.models import Student, Teacher


class Lesson(models.Model):
    """Довідка всіх дисциплін."""
    name = models.CharField('Назва', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'дисципліна'
        verbose_name_plural = 'Довідка дисципін'


class Grade(models.Model):
    """Довідка всіх груп."""
    number = models.SmallIntegerField('Число')
    symbol = models.CharField('Символ', max_length=5)
    lessons = models.ManyToManyField(Lesson, related_name='grade', verbose_name='Дисципліни групи')

    def __str__(self):
        return f'{self.symbol}-{self.number}'

    class Meta:
        verbose_name = 'група'
        verbose_name_plural = 'Довідка груп'


class RatingItemStatus(models.Model):
    """Довідка статусів оцінок."""
    name = models.CharField('Статус оцінки', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'статус оцінки'
        verbose_name_plural = 'Довідка статусів оцінок'


class GroupStudent(models.Model):
    """Групи студентів."""
    grade = models.OneToOneField(Grade, related_name='group', on_delete=models.CASCADE,
                                 verbose_name='Назва групи')
    create_group = models.DateField('Дата створення групи')
    updated = models.DateField('Дата оновлення', auto_now=True)
    created = models.DateField('Дата створення', auto_now_add=True)

    def __str__(self):
        return self.grade.__str__()

    def get_absolute_url(self):
        return reverse_lazy('group_student_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Група студнтів'
        verbose_name_plural = 'Групи студентів'


class Score(models.Model):
    """Журнал оцінок."""
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, verbose_name='Назва групи')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Дисципліна')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_student', on_delete=models.CASCADE,
                                limit_choices_to={'user_status': STUDENT}, verbose_name='Студент')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_teacher', on_delete=models.SET_NULL,
                                null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Викладач')
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name='Оцінка')
    score_status = models.ForeignKey(RatingItemStatus, on_delete=models.CASCADE, verbose_name='Статус оцінки')
    created = models.DateField(verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse_lazy('score_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'запис журналу'
        verbose_name_plural = 'Оцінки'
        unique_together = ['student', 'lesson', 'created']
