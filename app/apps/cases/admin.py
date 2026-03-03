from django.contrib import admin
from .models import CasesBanner, Cases


@admin.register(CasesBanner)
class CasesBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "term", "quantity", "result")
    search_fields = ("title", "type")