from test_task_bsl.celery import app
from test_task.models import Person
from django.db.models import F


@app.task
def payment():
    Person.objects.all().update(balance=F('balance') - F('hold'), hold=0)
