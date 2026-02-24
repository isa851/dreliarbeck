from django.db import models

class BookingRequest(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=50)
    service = models.CharField(max_length=120, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"