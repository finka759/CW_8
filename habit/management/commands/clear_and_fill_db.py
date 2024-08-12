from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from config.settings import TEST_CHAT_ID
from habit.models import Habit
from users.models import User


class Command(BaseCommand):
    """Команда для заполнения всех данных БД """

    def handle(self, *args, **options):
        Habit.objects.all().delete()
        User.objects.all().delete()

        user = User.objects.create(
            pk=1,
            email='admin',
            first_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()

        user_list = [
            {'pk': 2, 'fields':
                {'email': 'user2@sky.com', 'phone': '222222222', 'password': '222', 'chat_id': TEST_CHAT_ID}
             },
            {'pk': 3, 'fields':
                {'email': 'user3@sky.com', 'phone': '333333333', 'password': '333', 'chat_id': TEST_CHAT_ID}
             },
            {'pk': 4, 'fields':
                {'email': 'user4@sky.com', 'phone': '444444444', 'password': '444', 'chat_id': TEST_CHAT_ID}
             },
            {'pk': 5, 'fields':
                {'email': 'user5@sky.com', 'phone': '555555555', 'password': '555', 'chat_id': TEST_CHAT_ID}
             },
        ]
        users_for_create = []

        for user in user_list:
            users_for_create.append(
                User(pk=user.get('pk'),
                     email=user.get('fields').get('email'),
                     phone=user.get('fields').get('phone'),
                     password=make_password(user.get('fields').get('password')),
                     chat_id=user.get('fields').get('chat_id'),
                     )
            )

        User.objects.bulk_create(users_for_create)

        habit_list = [
            {'pk': 1, 'fields':
                {"place": None,
                 "time": "14:00:00",
                 "action": "action_plesant_habit_1",
                 "habit_is_pleasant": True,
                 "number_of_executions": 1,
                 "duration": "00:02:00",
                 "is_published": True,
                 "reward": None,
                 "user": 2,
                 "connection_habit": None, }
             },
            {'pk': 2, 'fields':
                {"place": None,
                 "time": "20:00:00",
                 "action": "action_plesant_habit_2",
                 "habit_is_pleasant": True,
                 "number_of_executions": 3,
                 "duration": "00:02:00",
                 "is_published": False,
                 "reward": None,
                 "user": 2,
                 "connection_habit": None, }
             },
            {'pk': 3, 'fields':
                {"place": None,
                 "time": "19:55:00",
                 "action": "action_plesant_habit_3",
                 "habit_is_pleasant": True,
                 "number_of_executions": 7,
                 "duration": "00:02:00",
                 "is_published": True,
                 "reward": None,
                 "user": 3,
                 "connection_habit": None, }
             },
        ]
        habits_for_create = []

        for habit in habit_list:
            habits_for_create.append(
                Habit(pk=habit.get('pk'),
                      user=User.objects.get(pk=habit.get('fields').get('user')),
                      place=habit.get('fields').get('place'),
                      time=habit.get('fields').get('time'),
                      action=habit.get('fields').get('action'),
                      habit_is_pleasant=habit.get('fields').get('habit_is_pleasant'),
                      number_of_executions=habit.get('fields').get('number_of_executions'),
                      duration=habit.get('fields').get('duration'),
                      is_published=habit.get('fields').get('is_published'),
                      reward=habit.get('fields').get('reward'),
                      )
            )
        Habit.objects.bulk_create(habits_for_create)

        habit_list2 = [
            {'pk': 4, 'fields':
                {"place": None,
                 "time": "21:36:00",
                 "action": "action_notplesant_habit_4",
                 "habit_is_pleasant": False,
                 "number_of_executions": 1,
                 "duration": "00:02:00",
                 "is_published": True,
                 "reward": None,
                 "user": 2,
                 "connection_habit": 1, }
             },
            {'pk': 5, 'fields':
                {"place": None,
                 "time": "21:37:00",
                 "action": "action_notplesant_habit_5",
                 "habit_is_pleasant": False,
                 "number_of_executions": 3,
                 "duration": "00:02:00",
                 "is_published": False,
                 "reward": None,
                 "user": 2,
                 "connection_habit": 2, }
             },
            {'pk': 6, 'fields':
                {"place": None,
                 "time": "21:38:00",
                 "action": "action_notplesant_habit_6",
                 "habit_is_pleasant": False,
                 "number_of_executions": 7,
                 "duration": "00:02:00",
                 "is_published": True,
                 "reward": None,
                 "user": 3,
                 "connection_habit": 3, }
             },
            {'pk': 7, 'fields':
                {"place": None,
                 "time": "21:39:00",
                 "action": "action_notplesant_habit_7",
                 "habit_is_pleasant": False,
                 "number_of_executions": 3,
                 "duration": "00:02:00",
                 "is_published": False,
                 "reward": "reward_7",
                 "user": 2,
                 "connection_habit": 2, }
             },
        ]
        habits_for_create2 = []

        for habit in habit_list2:
            habits_for_create2.append(
                Habit(pk=habit.get('pk'),
                      user=User.objects.get(pk=habit.get('fields').get('user')),
                      place=habit.get('fields').get('place'),
                      time=habit.get('fields').get('time'),
                      action=habit.get('fields').get('action'),
                      habit_is_pleasant=habit.get('fields').get('habit_is_pleasant'),
                      number_of_executions=habit.get('fields').get('number_of_executions'),
                      duration=habit.get('fields').get('duration'),
                      is_published=habit.get('fields').get('is_published'),
                      reward=habit.get('fields').get('reward'),
                      connection_habit=Habit.objects.get(pk=habit.get('fields').get('connection_habit')),
                      )
            )

        Habit.objects.bulk_create(habits_for_create2)
