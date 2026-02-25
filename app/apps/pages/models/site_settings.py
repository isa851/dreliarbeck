from django.db import models
from .base import TimeStampedModel


class SiteSettings(TimeStampedModel):
    phone = models.CharField(max_length=50, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")
    weekdays = models.CharField(max_length=120, blank=True, verbose_name="Режим работы в будние дни")
    weekends = models.CharField(max_length=120, blank=True, verbose_name="Режим работы в выходные дни")

    instagram = models.URLField(blank=True, verbose_name="Instagram")
    telegram = models.URLField(blank=True, verbose_name="Telegram")
    whatsapp = models.URLField(blank=True, verbose_name="WhatsApp")
    youtube = models.URLField(blank=True, verbose_name="YouTube")
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"