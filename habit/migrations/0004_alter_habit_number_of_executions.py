# Generated by Django 4.2.2 on 2024-08-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='number_of_executions',
            field=models.IntegerField(default=7, verbose_name='количество выполнений в неделю'),
        ),
    ]
