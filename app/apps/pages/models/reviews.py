from django.db import models
from .base import TimeStampedModel


class Review(TimeStampedModel):
    text = models.TextField(verbose_name="Текст")
    author_name = models.CharField(max_length=120, verbose_name="Автор")
    rating = models.FloatField(default=5, verbose_name="Оценка")
    avatar = models.ImageField(upload_to="reviews/", blank=True, null=True, verbose_name="Аватар")
    
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ["order"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        return self.author_name