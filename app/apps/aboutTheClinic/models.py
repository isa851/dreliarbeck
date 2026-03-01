from django.db import models

class AboutTheClinicBanner(models.Model):
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    title_our_team = models.CharField(max_length=120, verbose_name="Заголовок Наша команда")
    description_our_team = models.TextField(verbose_name="Описание Наша команда")

    title_philosophy = models.CharField(max_length=120, verbose_name="Заголовок Философия")
    description_philosophy = models.TextField(verbose_name="Описание Философия")

    title_interior = models.CharField(max_length=120, verbose_name="Заголовок Интерьер")
    description_interior = models.TextField(verbose_name="Описание Интерьер")

    title_certificates = models.CharField(max_length=120, verbose_name="Заголовок Сертификаты")
    description_certificates = models.TextField(verbose_name="Описание Сертификаты")

    title_recors = models.CharField(max_length=120, verbose_name="Заголовок Познакомимся лично?")
    description_recors = models.TextField(verbose_name="Описание Познакомимся лично?")
    
    class Meta:
        verbose_name = "Баннер О клинике"
        verbose_name_plural = "Баннеры О клинике"
    
    def __str__(self):
        return self.title

class AboutTheClinicDoctor(models.Model):
    photo_doctor = models.ImageField(upload_to="about_the_clinic/", verbose_name="Фото врача")
    doctor_position = models.CharField(max_length=120, verbose_name="Должность")
    doctor_name = models.CharField(max_length=120, verbose_name="Имя врача")
    doctor_subtitle = models.CharField(max_length=120, verbose_name="Подзаголовок")
    doctor_description = models.TextField(verbose_name="Описание")
    patients = models.IntegerField(verbose_name="Количество пациентов")
    experience = models.IntegerField(verbose_name="Стаж работы")
    courses = models.IntegerField(verbose_name="Количество курсов")
    recommend = models.IntegerField(verbose_name="Рекомендаций")

    
    class Meta:
        verbose_name = "Врач клиники"
        verbose_name_plural = "Врачи клиники"
    
    def __str__(self):
        return self.doctor_name

class AboutTheClinicOurTeam(models.Model):
    photo = models.ImageField(upload_to="about_the_clinic/", verbose_name="Фото")
    name = models.CharField(max_length=120, verbose_name="Имя")
    position = models.CharField(max_length=120, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"
    
    def __str__(self):
        return self.name


class AboutTheClinicPhilosophy(models.Model):
    icon = models.ImageField(upload_to="about_the_clinic/", verbose_name="Иконка")
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Философия"
        verbose_name_plural = "Философия"
    
    def __str__(self):
        return self.title

class AboutTheClinicInterior(models.Model):
    photo = models.ImageField(upload_to="about_the_clinic/", verbose_name="Фото")
    
    class Meta:
        verbose_name = "Интерьер"
        verbose_name_plural = "Интерьеры"
    
    def __str__(self):
        return "Интерьер"

class AboutTheClinicCertificates(models.Model):
    icon = models.ImageField(upload_to="about_the_clinic/", verbose_name="Иконка")
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    
    class Meta:
        verbose_name = "Сертификаты"
        verbose_name_plural = "Сертификаты"
    
    def __str__(self):
        return "Сертификаты"
