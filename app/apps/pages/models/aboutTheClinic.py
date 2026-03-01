from django.db import models
from .base import TimeStampedModel


class AboutTheClinic(TimeStampedModel):
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    philosophy_title = models.CharField(max_length=120, verbose_name="Заголовок философии")
    philosophy_description = models.TextField(verbose_name="Описание философии")

    interior_title = models.CharField(max_length=120, verbose_name="Заголовок интерьера")
    interior_description = models.TextField(verbose_name="Описание интерьера")

    certificates_title = models.CharField(max_length=120, verbose_name="Заголовок сертификатов")
    certificates_description = models.TextField(verbose_name="Описание сертификатов")

    personally_title = models.CharField(max_length=120, verbose_name="Заголовок персонально")
    personally_description = models.TextField(verbose_name="Описание персонально")

    class Meta:
        verbose_name = "О клинике"
        verbose_name_plural = "О клинике"

    def __str__(self):
        return self.title


# ==========================
# ФИЛОСОФИЯ
# ==========================

class Philosophy(models.Model):
    about = models.ForeignKey(
        AboutTheClinic,
        on_delete=models.CASCADE,
        related_name="philosophies",
        verbose_name="Клиника",
        null=True,
        blank=True
    )

    icon = models.ImageField(
        upload_to="about_the_clinic/philosophy/",
        blank=True,
        null=True,
        verbose_name="Иконка"
    )

    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Философия"
        verbose_name_plural = "Философия"

    def __str__(self):
        return self.title


# ==========================
# ИНТЕРЬЕР
# ==========================

class Interior(models.Model):
    about = models.ForeignKey(
        AboutTheClinic,
        on_delete=models.CASCADE,
        related_name="interiors",
        verbose_name="Клиника",
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="about_the_clinic/interior/",
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Интерьер"
        verbose_name_plural = "Интерьер"

    def __str__(self):
        return "Интерьер"


# ==========================
# СЕРТИФИКАТЫ
# ==========================

class Certificates(models.Model):
    about = models.ForeignKey(
        AboutTheClinic,
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name="Клиника",
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="about_the_clinic/certificates/",
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title