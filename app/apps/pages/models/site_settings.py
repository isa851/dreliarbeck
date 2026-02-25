from django.db import models
from .base import TimeStampedModel


class SiteSettings(TimeStampedModel):
    brand_name = models.CharField(
        max_length=120,
        default="Dr. Eliyar",
        verbose_name="Название бренда",
    )
    brand_tagline = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Подпись бренда",
    )

    phone = models.CharField(max_length=50, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")
    work_time = models.CharField(max_length=120, blank=True, verbose_name="Время работы")

    instagram = models.URLField(blank=True, verbose_name="Instagram")
    telegram = models.URLField(blank=True, verbose_name="Telegram")
    whatsapp = models.URLField(blank=True, verbose_name="WhatsApp")

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self) -> str:
        return self.brand_name