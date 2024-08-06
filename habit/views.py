from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Делаем текущего пользователя 'Создателем' привычки."""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
