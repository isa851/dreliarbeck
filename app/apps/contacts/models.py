from django.db import models


class ContactsBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title


class ContactsInfo(models.Model):
    addres = models.CharField(max_length=255, verbose_name="Адрес")
    landmark = models.CharField(max_length=255, verbose_name="Ориентир")

    weekdays = models.CharField(max_length=255, verbose_name="Пн–Пт")
    saturday = models.CharField(max_length=255, verbose_name="Суббота")
    sunday = models.CharField(max_length=255, verbose_name="Воскресенье")

    phone = models.CharField(max_length=255, verbose_name="Телефон")

    whatsapp = models.URLField(max_length=255, verbose_name="WhatsApp")
    telegram = models.URLField(max_length=255, verbose_name="Telegram")
    instagram = models.URLField(max_length=255, verbose_name="Instagram")

    map = models.TextField(verbose_name="Карта (iframe)", blank=True)

    def __str__(self):
        return self.addres


# 🔥 НОВАЯ МОДЕЛЬ
class Booking(models.Model):
    SERVICE_CHOICES = [
        ("Консультация", "Консультация"),
        ("Имплантация", "Имплантация"),
        ("Виниры / Коронки", "Виниры / Коронки"),
        ("Лечение кариеса", "Лечение кариеса"),
        ("Ортодонтия", "Ортодонтия"),
        ("Хирургия", "Хирургия"),
        ("Гигиена / Отбеливание", "Гигиена / Отбеливание"),
        ("Детская стоматология", "Детская стоматология"),
        ("Другое", "Другое"),
    ]

    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    service = models.CharField(
        max_length=255,
        choices=SERVICE_CHOICES,
        verbose_name="Услуга"
    )
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запись на приём"
        verbose_name_plural = "Записи на приём"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.phone}"