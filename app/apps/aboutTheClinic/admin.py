from django.contrib import admin
from .models import (
    AboutTheClinicBanner,
    AboutTheClinicCertificates,
    AboutTheClinicDoctor,
    AboutTheClinicInterior,
    AboutTheClinicOurTeam,
    AboutTheClinicPhilosophy,
)

# ===============================
# БАННЕР (только одна запись)
# ===============================

@admin.register(AboutTheClinicBanner)
class AboutTheClinicBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        if AboutTheClinicBanner.objects.exists():
            return False
        return True


# ===============================
# ВРАЧ
# ===============================

@admin.register(AboutTheClinicDoctor)
class AboutTheClinicDoctorAdmin(admin.ModelAdmin):
    list_display = (
        "doctor_name",
        "doctor_position",
        "experience",
        "patients",
    )
    search_fields = ("doctor_name", "doctor_position")
    list_filter = ("experience",)
    ordering = ("doctor_name",)


# ===============================
# НАША КОМАНДА
# ===============================

@admin.register(AboutTheClinicOurTeam)
class AboutTheClinicOurTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    ordering = ("name",)


# ===============================
# ФИЛОСОФИЯ
# ===============================

@admin.register(AboutTheClinicPhilosophy)
class AboutTheClinicPhilosophyAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


# ===============================
# ИНТЕРЬЕР
# ===============================

@admin.register(AboutTheClinicInterior)
class AboutTheClinicInteriorAdmin(admin.ModelAdmin):
    list_display = ("id",)


# ===============================
# СЕРТИФИКАТЫ
# ===============================

@admin.register(AboutTheClinicCertificates)
class AboutTheClinicCertificatesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)