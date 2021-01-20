import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task_bsl.settings')

app = Celery('test_task_bsl')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task-name': {
        'task': 'test_task.tasks.payment',
        'schedule': timedelta(minutes=10),
    }
}
