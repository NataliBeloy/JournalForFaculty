# Generated by Django 3.0.8 on 2022-05-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20220516_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='study_degree',
            field=models.CharField(choices=[('Бакалавр', 'Бакалавр'), ('Магістр', 'Магістр')], default=0, max_length=30, verbose_name='Ступінь навчання'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='study_form',
            field=models.CharField(choices=[('Бюджет', 'Бюджет'), ('Контракт', 'Контракт')], max_length=20, verbose_name='Форма навчання'),
        ),
    ]