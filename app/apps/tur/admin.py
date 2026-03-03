from django.contrib import admin
from .models import TurBanner, TurClinik


@admin.register(TurBanner)
class TurBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(TurClinik)
class TurClinikAdmin(admin.ModelAdmin):
    list_display = ("title",)