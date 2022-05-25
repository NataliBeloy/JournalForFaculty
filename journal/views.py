from datetime import datetime
from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from django_journal.permissions import TeacherPermissionsMixin, TeacherLessonPermissionsMixin
from django_journal.settings import TEACHER
from people.models import User
from utils.service import ScoreJournalMixin
from .models import GroupStudent, Score, Lesson


class CreateReport(LoginRequiredMixin, View):

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        d = datetime.today().strftime('%Y-%m-%d')
        response['Content-Disposition'] = f'inline; filename="{d}.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)

        # Data to print
        data = {
            "Posts": [{"title": "Python", "views": 500}, {"title": "JavaScript", "views": 500}],
            "Videos": [{"title": "Python Programming", "likes": 500}],
            "Blogs": [{"name": "Report Lab", "likes": 500, "claps": 500}],
        }

        p.setFont("Helvetica", 14, leading=None)
        p.setFillColorRGB(0.29296875, 0.453125, 0.609375)
        p.drawString(260, 800, "My PDF")
        p.line(0, 780, 1000, 780)
        p.line(0, 778, 1000, 778)
        xl = 20
        yl = 750

        for k, v in data.items():
            p.setFont("Helvetica", 14, leading=None)
            p.drawString(xl, yl - 12, f"{k}")
            for value in v:
                for key, val in value.items():
                    p.setFont("Helvetica", 12, leading=None)
                    p.drawString(xl, yl - 20, f"{key} - {val}")
                    yl = yl - 60
        p.setTitle(f'Report on {d}')
        p.showPage()
        p.save()

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response


class GroupStudentListView(LoginRequiredMixin, TeacherPermissionsMixin, ListView):
    """Список груп"""
    template_name = 'journal/group_list.html'
    context_object_name = 'users_teachers'

    def get_queryset(self):
        queryset = User.objects.select_related('teacher__group_manager__grade').filter(user_status=TEACHER)
        return queryset


class GroupStudentDetailView(LoginRequiredMixin, TeacherPermissionsMixin, DetailView):
    """Інформація про групу."""
    model = GroupStudent
    template_name = 'journal/group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super(GroupStudentDetailView, self).get_context_data()
        context['students'] = User.objects.select_related('student__group') \
            .filter(student__group_id=self.kwargs['pk'])
        return context


class ScoreLessonListView(LoginRequiredMixin, TeacherLessonPermissionsMixin, ScoreJournalMixin, ListView):
    """Журнал оцінок групи по дисципліні."""
    template_name = 'journal/journal_lesson_list.html'
    context_object_name = 'scores'
    permission_denied_message = 'В доступу відмовлено'

    def get_queryset(self):
        group_student = GroupStudent.objects.select_related('grade')
        self.group = get_object_or_404(group_student, id=self.kwargs['group_id'])
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        queryset = Score.objects.select_related('group', 'lesson') \
            .filter(group_id=self.kwargs['group_id'], lesson_id=self.kwargs['lesson_id'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ScoreLessonListView, self).get_context_data(**kwargs)
        date_period = self.create_date_period_list()
        students = User.objects.select_related('student', 'student__group').filter(student__group=self.group)

        scores = Score.objects.select_related('group', 'lesson') \
            .filter(created__in=date_period, lesson_id=self.lesson, group_id=self.group)

        context['date_period'] = date_period
        context['students'] = students
        context['scores_dict'] = self.create_scores_dict(date_period,
                                                         scores.values('id', 'student', 'score', 'created'),
                                                         students, 'student')
        context['group'] = self.group
        context['lesson'] = self.lesson
        return context


class AddScore(LoginRequiredMixin, TeacherLessonPermissionsMixin, View):
    """Додавання оцінки."""

    def post(self, request):
        score_id = request.POST.get('score_id')
        if score_id == '0':
            score_id = None
        score_params = {
            'score': request.POST.get('score_value'),
            'group_id': request.POST.get('group'),
            'lesson_id': request.POST.get('lesson'),
            'student_id': request.POST.get('student'),
            'teacher_id': request.POST.get('teacher'),
            'score_status_id': request.POST.get('score_status'),
            'created': request.POST.get('score_date'),
        }

        if score_params['score']:
            Score.objects.update_or_create(id=score_id, defaults=score_params)
            return JsonResponse({'status': 'ok'})
        else:
            Score.objects.get(id=score_id).delete()
            return JsonResponse({'status': 'ok'})
