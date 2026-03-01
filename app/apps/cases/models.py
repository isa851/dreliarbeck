from tabnanny import verbose
from unittest import result
from django.db import models

class CasesBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    title_record = models.CharField(max_length=255,verbose_name="Название Хотите такой же результат?")
    description_record = models.TextField(verbose_name="Описание Хотите такой же результат?")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class Cases(models.Model):
    imageOne = models.ImageField(upload_to="cases/", verbose_name="Изображение 1")
    imageTwo = models.ImageField(upload_to="cases/",verbose_name="Изображение 2")
    type = models.CharField(max_length=255, verbose_name="Тип")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    term = models.CharField(max_length=255, verbose_name="Срок")
    quantity = models.CharField(max_length=255, verbose_name="Количество")
    result = models.CharField(max_length=255, verbose_name="Результат")

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"