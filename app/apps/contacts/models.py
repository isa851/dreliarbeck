from django.db import models

class ContactsBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title
    


class ContactsInfo(models.Model):
    addres = models.CharField(max_length=255, verbose_name="Адрес")
    landmark = models.CharField(max_length=255, verbose_name="Ориентир")

    weekdays = models.CharField(max_length=255,verbose_name="Пн–Пт")
    saturday = models.CharField(max_length=255,verbose_name="Суббота")
    sunday = models.CharField(max_length=255,verbose_name="Воскресенье")

    phone = models.CharField(max_length=255,verbose_name="Телефон")


    whatsapp = models.URLField(max_length=255,verbose_name="WhatsApp")
    telegram = models.URLField(max_length=255,verbose_name="Telegram")
    instagram = models.URLField(max_length=255,verbose_name="инстаграм")


    map = models.TextField(verbose_name="Карта (iframe)", blank=True)
    
    def __str__(self):
        return self.addres
    