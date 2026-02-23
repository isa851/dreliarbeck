from django.db import models



class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено"
    )

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    brand_name = models.CharField(
        max_length=120,
        default="Dr. Eliyar",
        verbose_name="Название бренда"
    )
    brand_tagline = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Подпись бренда"
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Телефон"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="Email"
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Адрес"
    )
    work_time = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Время работы"
    )

    instagram = models.URLField(
        blank=True,
        verbose_name="Instagram"
    )
    telegram = models.URLField(
        blank=True,
        verbose_name="Telegram"
    )
    whatsapp = models.URLField(
        blank=True,
        verbose_name="WhatsApp"
    )

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return self.brand_name



class HomePage(TimeStampedModel):

    hero_badge = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Бейдж"
    )

    hero_title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )

    hero_subtitle = models.TextField(
        blank=True,
        verbose_name="Подзаголовок"
    )

    hero_bg = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        verbose_name="Фон"
    )

    cta_primary_text = models.CharField(
        max_length=50,
        default="Записаться",
        verbose_name="Первая кнопка"
    )

    cta_primary_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL первой кнопки"
    )

    cta_secondary_text = models.CharField(
        max_length=50,
        default="Посмотреть 360° тур",
        verbose_name="Вторая кнопка"
    )

    cta_secondary_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL второй кнопки"
    )

    trust_title = models.CharField(
        max_length=120,
        default="Почему нам доверяют",
        verbose_name="Заголовок доверия"
    )

    trust_subtitle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Подзаголовок доверия"
    )

    services_title = models.CharField(
        max_length=120,
        default="Наши услуги",
        verbose_name="Заголовок услуг"
    )

    services_subtitle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Подзаголовок услуг"
    )

    services_all_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL всех услуг"
    )

    tour_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Заголовок тура"
    )

    tour_subtitle = models.TextField(
        blank=True,
        verbose_name="Подзаголовок тура"
    )

    tour_image = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        verbose_name="Фото тура"
    )

    tour_url = models.URLField(
        blank=True,
        verbose_name="URL тура"
    )

    final_cta_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Заголовок CTA"
    )

    final_cta_text = models.TextField(
        blank=True,
        verbose_name="Текст CTA"
    )

    final_cta_primary_text = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Первая кнопка CTA"
    )

    final_cta_primary_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL первой CTA"
    )

    final_cta_secondary_text = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Вторая CTA"
    )

    final_cta_secondary_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL второй CTA"
    )

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    def __str__(self):
        return "Home Page"



class HomeStat(models.Model):

    home = models.ForeignKey(
        HomePage,
        related_name="stats",
        on_delete=models.CASCADE
    )

    value = models.CharField(
        max_length=30,
        verbose_name="Значение"
    )

    label = models.CharField(
        max_length=80,
        verbose_name="Подпись"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"



class HomeFeature(models.Model):

    home = models.ForeignKey(
        HomePage,
        related_name="features",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=120)

    text = models.TextField()

    icon = models.CharField(
        max_length=50,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"




class Service(TimeStampedModel):

    title = models.CharField(max_length=120)

    description = models.TextField(blank=True)

    price_from = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    currency = models.CharField(
        max_length=10,
        default="сум"
    )

    icon = models.CharField(
        max_length=50,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class DoctorProfile(TimeStampedModel):

    name = models.CharField(max_length=120)

    role = models.CharField(max_length=120, blank=True)

    specialty = models.CharField(max_length=255, blank=True)

    description = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="doctor/",
        blank=True,
        null=True
    )

    details_url = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return self.name


class DoctorFact(models.Model):

    doctor = models.ForeignKey(
        DoctorProfile,
        related_name="facts",
        on_delete=models.CASCADE
    )

    text = models.CharField(max_length=200)

    icon = models.CharField(max_length=50, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Факт"
        verbose_name_plural = "Факты"



class Case(TimeStampedModel):

    tag = models.CharField(max_length=80, blank=True)

    duration = models.CharField(max_length=80, blank=True)

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

    def __str__(self):
        return self.title


class CaseImage(models.Model):

    BEFORE = "before"
    AFTER = "after"

    KIND_CHOICES = [
        (BEFORE, "Before"),
        (AFTER, "After"),
    ]

    case = models.ForeignKey(
        Case,
        related_name="images",
        on_delete=models.CASCADE
    )

    kind = models.CharField(
        max_length=10,
        choices=KIND_CHOICES
    )

    image = models.ImageField(
        upload_to="cases/"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото кейса"
        verbose_name_plural = "Фото кейсов"


class Review(TimeStampedModel):

    text = models.TextField()

    author_name = models.CharField(max_length=120)

    rating = models.PositiveSmallIntegerField(default=5)

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.author_name