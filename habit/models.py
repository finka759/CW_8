from django.db import models
from datetime import timedelta
from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        **NULLABLE
    )
    action = models.CharField(
        max_length=100,
        verbose_name="действие"
    )
    place = models.CharField(
        max_length=100,
        verbose_name="место выполнения",
        **NULLABLE
    )
    time = models.TimeField(
        verbose_name="время выполнения",
        ** NULLABLE
    )
    habit_is_pleasant = models.BooleanField(
        default=True,
        verbose_name="признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        **NULLABLE,
    )
    number_of_executions = models.IntegerField(
        default=1,
        verbose_name="количество выполнений в неделю"
    )
    duration = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="продолжительность выполнения"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="признак публичности")
    reward = models.CharField(
        max_length=100,
        verbose_name="вознаграждение",
        **NULLABLE,
    )

    def __str__(self):
        return f"Действие: {self.action}(юзер {self.user})"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
