# Generated by Django 3.0.8 on 2022-04-20 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(limit_choices_to={'user_status': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='score_student', to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='score',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'user_status': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='score_teacher', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='grade',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='journal.Grade', verbose_name='Наименование класса'),
        ),
        migrations.AddField(
            model_name='grade',
            name='lessons',
            field=models.ManyToManyField(related_name='grade', to='journal.Lesson', verbose_name='Уроки класса'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('student', 'lesson', 'created')},
        ),
    ]
