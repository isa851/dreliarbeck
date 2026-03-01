from django.db import models
from .base import TimeStampedModel




class DoctorProfile(TimeStampedModel):
    name = models.CharField(max_length=120, verbose_name="Имя")
    role = models.CharField(max_length=120, blank=True, verbose_name="Должность")
    description = models.TextField(blank=True, verbose_name="Описание")
    subtitle = models.CharField(max_length=20, blank=True, verbose_name="Подзаголовок")
    photo = models.ImageField(upload_to="doctor/", blank=True, null=True, verbose_name="Фото")
    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self) -> str:
        return self.name


