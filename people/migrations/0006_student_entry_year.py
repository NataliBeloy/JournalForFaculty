# Generated by Django 3.0.8 on 2022-05-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20220517_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='entry_year',
            field=models.IntegerField(default=0, max_length=4, verbose_name='Рік вступу'),
            preserve_default=False,
        ),
    ]
