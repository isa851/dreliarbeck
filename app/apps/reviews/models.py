from django.db import models


class ReviewBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    record_title = models.CharField(max_length=255, verbose_name="Название Присоединяйтесь к 5 000+ довольных пациентов")
    description_record = models.TextField(verbose_name="Описание Присоединяйтесь к 5 000+ довольных пациентов")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class Review(models.Model):
    patients = models.IntegerField(verbose_name="Количество пациентов")
    average_rating = models.IntegerField(verbose_name="средний рейтинг ")
    recommend = models.IntegerField(verbose_name="рекомендуют нас")
    reviews_online = models.IntegerField(verbose_name="отзывов онлайн")


    vidio = models.FileField(upload_to="reviews/vidio/", verbose_name="Видео")
    title_vidio = models.CharField(max_length=255,verbose_name="Название")


    text_rating = models.FloatField(verbose_name="рейтинга")
    text_description = models.TextField(verbose_name="Описание")
    avatar =  models.ImageField(upload_to="reviews/", verbose_name="Аватар")
    author = models.CharField(max_length=255, verbose_name="Автор")
    time = models.CharField(max_length=255, verbose_name="Время")