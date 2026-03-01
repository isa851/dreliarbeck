from django.db import models



class TurBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    title_clinik = models.CharField(max_length=255, verbose_name="Название что внутри клиники ")
    description_clinik  = models.TextField(verbose_name="Описание что внутри клиники")

    record_title = models.CharField(max_length=255,verbose_name=" название Хотите увидеть клинику лично?")
    record_description = models.TextField(verbose_name="Описание Хотите увидеть клинику лично?")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class TurClinik(models.Model):
    icon = models.ImageField(upload_to='tur_clinik/', verbose_name="Иконка")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"