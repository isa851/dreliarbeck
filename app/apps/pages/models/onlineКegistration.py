from django.db import models
from .base import TimeStampedModel

class ChatBooking(TimeStampedModel):
    problem = models.CharField(max_length=255,verbose_name="Проблема")
    date = models.CharField(max_length=255,verbose_name="Дата")
    fear = models.CharField(max_length=255,verbose_name="Страх")
    name = models.CharField(max_length=255,verbose_name="Имя")
    phone = models.CharField(max_length=255,verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись в чат"
        verbose_name_plural = "Записи в чат"
