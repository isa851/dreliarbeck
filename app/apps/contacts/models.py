from django.db import models

class AppointmentRequest(models.Model):
    SOURCE_CHOICES = [
        ("hero", "Hero button"),
        ("services", "Service card"),
        ("quick", "Quick widget"),
        ("cta", "Final CTA"),
        ("call", "Call button"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    reason = models.CharField(max_length=80, blank=True) 
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="other")

    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone} ({self.source})"