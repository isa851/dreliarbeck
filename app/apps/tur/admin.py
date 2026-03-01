from django.contrib import admin

from apps.tur.models import TurBanner, TurClinik

@admin.register(TurBanner)
class TurBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(TurClinik)
class TurClinikAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']