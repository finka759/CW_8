from rest_framework.serializers import ModelSerializer

from habit.models import Habit
from habit.validators import TimeDurationValidator, NotCombinationValidator, CombinationValidator, AbsenceValidator, \
    FrequencyValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            TimeDurationValidator("duration"),
            NotCombinationValidator("connection_habit", "reward"),
            CombinationValidator("connection_habit"),
            AbsenceValidator("habit_is_pleasant", "connection_habit", "reward"),
            FrequencyValidator("number_of_executions"),
        ]
