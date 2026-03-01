from django.db import models
from django.utils.text import slugify

class ServicesBanner(models.Model):
    title = models.CharField(max_length=255,verbose_name="название")
    description = models.TextField(verbose_name="описание")

    record_service_title = models.CharField(max_length=255, verbose_name="название записи")
    record_service_description = models.TextField(verbose_name="описание записи")



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "баннер услуги"

class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name="название услуги")
    description = models.TextField(verbose_name="описание услуги")
    slug = models.SlugField(unique=True, blank=True)
    price = models.IntegerField(verbose_name="цена услуги")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"



class ServicesHome(models.Model):
    photo = models.ImageField(
        upload_to="services_home/",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга на главной"
        verbose_name_plural = "Услуги на главной"