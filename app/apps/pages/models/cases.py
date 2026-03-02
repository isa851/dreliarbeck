from django.db import models
from .base import TimeStampedModel


class ResultsIndex(TimeStampedModel):
    tag = models.CharField(max_length=80, blank=True, verbose_name="Тег")
    duration = models.CharField(max_length=80, blank=True, verbose_name="Длительность")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")

    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ["order"]
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

    def __str__(self) -> str:
        return self.title


class ResultsIndexImage(models.Model):
    BEFORE = "before"
    AFTER = "after"

    KIND_CHOICES = [
        (BEFORE, "Before"),
        (AFTER, "After"),
    ]

    case = models.ForeignKey(ResultsIndex, related_name="images", on_delete=models.CASCADE)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, verbose_name="Тип")
    image = models.ImageField(upload_to="cases/", verbose_name="Фото")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото кейса"
        verbose_name_plural = "Фото кейсов"

    def __str__(self) -> str:
        return f"{self.case_id} — {self.kind}"