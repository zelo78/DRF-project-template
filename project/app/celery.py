import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

celery_app = Celery("app")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    # Название задачи
    "my-super-sum-every-5-min": {
        # Регистрируем задачу. Для этого в качестве значения ключа task
        # Указываем полный путь до созданного нами ранее таска(функции)
        "task": "main.tasks.supper_sum",
        # Периодичность с которой мы будем запускать нашу задачу
        # minute='*/5' - говорит о том, что задача должна выполнятся каждые 5 мин.
        "schedule": crontab(minute="*/5"),
        # Аргументы которые будет принимать функция
        "args": (5, 8),
    }
}
