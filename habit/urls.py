from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitListApiView, HabitRetrieveApiView, HabitCreateApiView, HabitDestroyApiView, \
    HabitUpdateApiView, HabitPublishedListApiView

app_name = HabitConfig.name

urlpatterns = [
    path("create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("list/", HabitListApiView.as_view(), name="habit_list"),
    path("published_list/", HabitPublishedListApiView.as_view(), name="published_habit_list"),
    path("<int:pk>/", HabitRetrieveApiView.as_view(), name="habit_one"),
    path("<int:pk>/delete/", HabitDestroyApiView.as_view(), name="habit_delete"),
    path("<int:pk>/update/", HabitUpdateApiView.as_view(), name="habit_update"),
]