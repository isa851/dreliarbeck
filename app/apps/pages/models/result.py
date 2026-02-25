from django.db import models
from .base import TimeStampedModel 


class Result(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок")
    type = models.CharField(max_length=255, blank=True, verbose_name="Тип результата")
    description = models.TextField(blank=True, verbose_name="Описание результата")
    image = models.ImageField(upload_to="result/", blank=True, null=True, verbose_name="Изображение")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    
    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    def __str__(self):
        return self.title