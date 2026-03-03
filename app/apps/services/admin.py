from django.contrib import admin
from .models import Services, ServicesBanner, ServicesHome


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "slug")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ServicesBanner)
class ServicesBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ServicesHome)
class ServicesHomeAdmin(admin.ModelAdmin):
    list_display = ("title",)