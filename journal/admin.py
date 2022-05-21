from django.contrib import admin

from journal.models import Lesson, Grade, RatingItemStatus, GroupStudent, Score


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Дисципліни."""
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """Групи."""
    list_display = ('number', 'symbol')


@admin.register(RatingItemStatus)
class RatingItemStatusAdmin(admin.ModelAdmin):
    """Статуси оцінок."""
    list_display = ('name',)


@admin.register(GroupStudent)
class GroupStudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """Оцінки."""
    list_display = ('student', 'lesson', 'score', 'created', 'updated', 'group')
    list_filter = ('created', 'score', 'lesson', 'group')
    search_fields = ('student__first_name', 'student__last_name')
    save_on_top = True
