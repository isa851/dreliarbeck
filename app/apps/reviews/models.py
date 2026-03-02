from django.db import models


class ReviewBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    record_title = models.CharField(
        max_length=255,
        verbose_name="Заголовок блока Присоединяйтесь"
    )
    description_record = models.TextField(
        verbose_name="Описание блока Присоединяйтесь"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class ReviewStats(models.Model):
    patients = models.IntegerField(verbose_name="Количество пациентов")
    average_rating = models.FloatField(verbose_name="Средний рейтинг")
    recommend = models.IntegerField(verbose_name="Процент рекомендаций")
    reviews_online = models.IntegerField(verbose_name="Отзывов онлайн")

    def __str__(self):
        return "Статистика отзывов"

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"


class Review(models.Model):
    avatar = models.ImageField(upload_to="reviews/", verbose_name="Аватар")
    author = models.CharField(max_length=255, verbose_name="Автор")
    time = models.CharField(max_length=255, verbose_name="Дата / Тип лечения")

    text_rating = models.FloatField(verbose_name="Рейтинг")
    text_description = models.TextField(verbose_name="Текст отзыва")

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Текстовый отзыв"
        verbose_name_plural = "Текстовые отзывы"


class VideoReview(models.Model):
    video = models.FileField(upload_to="reviews/video/", verbose_name="Видео")
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео отзыв"
        verbose_name_plural = "Видео отзывы"