# Generated by Django 3.0.8 on 2022-05-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_student_entry_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_work',
            field=models.CharField(default=0, max_length=100, verbose_name='Тема курсової роботи'),
            preserve_default=False,
        ),
    ]