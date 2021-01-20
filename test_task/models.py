import uuid
from django.db import models


# Create your models here.


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Фамилия')
    balance = models.IntegerField(null=False, blank=False, verbose_name='Баланс')
    hold = models.IntegerField(null=False, blank=False, verbose_name='Холд')
    status = models.BooleanField(default=False, verbose_name='Статус')
