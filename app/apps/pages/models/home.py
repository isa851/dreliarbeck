from django.db import models
from .base import TimeStampedModel


class HomePage(TimeStampedModel):
    hero_badge = models.CharField(max_length=120, blank=True, verbose_name="Бейдж")
    hero_title = models.CharField(max_length=200, verbose_name="Заголовок")
    hero_subtitle = models.TextField(blank=True, verbose_name="Подзаголовок")
    hero_bg = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        verbose_name="Фон",
    )

    trust_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок доверия")
    trust_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок доверия")

    services_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок услуг")
    services_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок услуг")

    our_command_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок команды")
    our_command_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок команды")

    tur_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок туров")
    tur_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок туров")

    doctor_name = models.CharField(max_length=255, blank=True, verbose_name="Имя доктора")
    doctor_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок доктора")
    doctor_description = models.TextField(blank=True, verbose_name="Описание доктора")
    doctor_photo = models.ImageField(upload_to="home/doctor/", blank=True, null=True, verbose_name="Фото доктора")

    doctor_patients = models.IntegerField(blank=True, null=True, verbose_name="Количество пациентов")
    doctor_experience = models.IntegerField(blank=True, null=True, verbose_name="Опыт работы")
    doctor_courses = models.IntegerField(blank=True, null=True, verbose_name="Количество курсов")
    doctor_recommend = models.IntegerField(blank=True, null=True, verbose_name="Количество рекомендаций")

    result_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок результата")
    result_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок результата")
    result_image = models.ImageField(
        upload_to="home/result/",
        blank=True,
        null=True,
        verbose_name="Изображение результата",
    )


    review_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок отзыва")
    review_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок отзыва")


    consultation_title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок консультации")
    consultation_subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок консультации")

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    def __str__(self) -> str:
        return "Home Page"


class HomeStat(models.Model):
    home = models.ForeignKey(HomePage, related_name="stats", on_delete=models.CASCADE)
    value = models.CharField(max_length=30, verbose_name="Значение")
    label = models.CharField(max_length=80, verbose_name="Подпись")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"

    def __str__(self) -> str:
        return f"{self.value} — {self.label}"


class HomeFeature(models.Model):
    home = models.ForeignKey(HomePage, related_name="features", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    icon = models.ImageField(upload_to="home/feature/", blank=True, null=True, verbose_name="Иконка")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self) -> str:
        return self.title
