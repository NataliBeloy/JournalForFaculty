# Generated by Django 3.0.8 on 2022-05-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20220420_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='symbol',
            field=models.CharField(max_length=5, verbose_name='Символ'),
        ),
    ]