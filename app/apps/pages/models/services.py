from django.db import models
from .base import TimeStampedModel


class Service(TimeStampedModel):
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    price_from = models.PositiveIntegerField(null=True, blank=True, verbose_name="Цена от")
    currency = models.CharField(max_length=10, default="сум", verbose_name="Валюта")

    icon = models.ImageField(upload_to="service/", blank=True, null=True, verbose_name="Иконка")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self) -> str:
        return self.title