from datetime import timedelta

from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase, APIClient

from config.settings import TEST_CHAT_ID
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестируем привычки."""

    def setUp(self):
        self.user = User.objects.create(email="ivan@example.com")

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

        for user in user_list:
            User.objects.create(pk=user.get('pk'),
                                email=user.get('fields').get('email'),
                                phone=user.get('fields').get('phone'),
                                password=make_password(user.get('fields').get('password')),
                                chat_id=user.get('fields').get('chat_id'),
                                )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            uzer=self.user,
            place="Рабочее место",
            time="14:00:00",
            action="Делать вид, что у тебя все хорошо",
            habit_is_pleasant=False,
            connection_habit=None,
            number_of_executions=5,
            duration=timedelta(seconds=120),
            is_published=True,
            reward="Взять с полки пирожок",
        )

    def test_habit_list(self):
        """Тестируем вывод списка привычек."""

        url = reverse("habit:habit_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_is_published_list(self):
        """Тестируем вывод списка публичных привычек."""

        url = reverse("habit:habit_is_published_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_create(self):
        """Тестируем создание привычки."""

        url = reverse("habit:habit_create")
        data = {
            "action": "Ничего не делать",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестируем изменение привычки."""

        url = reverse("habit:habit_update", args=(self.habit.pk,))
        data = {
            "reward": "Почесать за ухом",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "Почесать за ухом")

    def test_habit_delete(self):
        """Тестируем удаление привычки."""

        url = reverse("habit:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
