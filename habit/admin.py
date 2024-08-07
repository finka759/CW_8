from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Админка привычек"""
    list_display = (
        "id",
        "place",
        "time",
        "action",
        "habit_is_pleasant",
        "number_of_executions",
        "duration",
        "is_published",
        "reward",
        "user",
        "connection_habit",
    )
