import datetime

from habit.models import Habit

from celery import shared_task

from habit.services import message_create, send_tg


@shared_task
def send_message_tg():
    print('проверка времени начата')
    current_time = datetime.datetime.now().replace(second=0, microsecond=0)
    current_time_plus_5 = current_time + datetime.timedelta(minutes=5)

    habits = Habit.objects.filter(habit_is_pleasant=False)

    for habit in habits:
        if str(habit.time) == str(current_time_plus_5.strftime("%X")):
            # if habit.is_published:
            chat_id = habit.user.chat_id
            if chat_id:
                count = habit.number_of_executions
                if count != 0:
                    text_message = message_create(habit.pk)
                    send_tg(chat_id=chat_id, message=text_message)
                    count -= 1
                    habit.save()
