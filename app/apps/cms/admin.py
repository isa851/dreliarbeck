from django.contrib import admin
from django.utils.html import format_html

from .models import (
    SiteSettings,
    HomePage, HomeStat, HomeFeature,
    Service,
    DoctorProfile, DoctorFact,
    Case, CaseImage,
    Review,
)

# ---------- Общие утилиты ----------

class SingletonAdminMixin:
    """
    Делает модель "одной записью": нельзя добавить больше 1.
    Можно оставить только одну настройку/главную страницу.
    """
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


# ---------- SiteSettings ----------

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("brand_name", "phone", "email", "updated_at")
    search_fields = ("brand_name", "phone", "email", "address")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Бренд", {
            "fields": ("brand_name", "brand_tagline")
        }),
        ("Контакты", {
            "fields": ("phone", "email", "address", "work_time")
        }),
        ("Соцсети", {
            "fields": ("instagram", "telegram", "whatsapp")
        }),
        ("Служебное", {
            "fields": ("created_at", "updated_at")
        }),
    )


# ---------- HomePage + inline ----------

class HomeStatInline(admin.TabularInline):
    model = HomeStat
    extra = 0
    fields = ("value", "label", "order")
    ordering = ("order",)


class HomeFeatureInline(admin.TabularInline):
    model = HomeFeature
    extra = 0
    fields = ("title", "text", "icon", "order")
    ordering = ("order",)


@admin.register(HomePage)
class HomePageAdmin(SingletonAdminMixin, admin.ModelAdmin):
    inlines = (HomeStatInline, HomeFeatureInline)

    list_display = ("__str__", "hero_title", "updated_at")
    search_fields = ("hero_title", "hero_badge", "trust_title", "services_title")
    readonly_fields = ("created_at", "updated_at", "hero_bg_preview", "tour_image_preview")

    fieldsets = (
        ("Hero", {
            "fields": (
                "hero_badge",
                "hero_title",
                "hero_subtitle",
                ("hero_bg", "hero_bg_preview"),
            )
        }),
        ("Кнопки (CTA)", {
            "fields": (
                ("cta_primary_text", "cta_primary_url"),
                ("cta_secondary_text", "cta_secondary_url"),
            )
        }),
        ("Блок доверия", {
            "fields": ("trust_title", "trust_subtitle")
        }),
        ("Услуги", {
            "fields": ("services_title", "services_subtitle", "services_all_url")
        }),
        ("Тур", {
            "fields": (
                "tour_title",
                "tour_subtitle",
                ("tour_image", "tour_image_preview"),
                "tour_url",
            )
        }),
        ("Финальный CTA", {
            "fields": (
                "final_cta_title",
                "final_cta_text",
                ("final_cta_primary_text", "final_cta_primary_url"),
                ("final_cta_secondary_text", "final_cta_secondary_url"),
            )
        }),
        ("Служебное", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def hero_bg_preview(self, obj):
        if obj and obj.hero_bg:
            return format_html('<img src="{}" style="max-height:120px;border-radius:8px;" />', obj.hero_bg.url)
        return "—"
    hero_bg_preview.short_description = "Превью фона"

    def tour_image_preview(self, obj):
        if obj and obj.tour_image:
            return format_html('<img src="{}" style="max-height:120px;border-radius:8px;" />', obj.tour_image.url)
        return "—"
    tour_image_preview.short_description = "Превью тура"


# ---------- Service ----------

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price_from", "currency", "is_active", "order", "updated_at")
    list_filter = ("is_active", "currency")
    search_fields = ("title", "description")
    list_editable = ("is_active", "order")
    ordering = ("order",)
    readonly_fields = ("created_at", "updated_at")


# ---------- DoctorProfile + inline ----------

class DoctorFactInline(admin.TabularInline):
    model = DoctorFact
    extra = 0
    fields = ("text", "icon", "order")
    ordering = ("order",)


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    inlines = (DoctorFactInline,)

    list_display = ("name", "role", "specialty", "photo_preview", "updated_at")
    search_fields = ("name", "role", "specialty", "description")
    readonly_fields = ("created_at", "updated_at", "photo_preview")
    fieldsets = (
        ("Основное", {
            "fields": ("name", "role", "specialty", "description")
        }),
        ("Фото", {
            "fields": ("photo", "photo_preview")
        }),
        ("Ссылка", {
            "fields": ("details_url",)
        }),
        ("Служебное", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def photo_preview(self, obj):
        if obj and obj.photo:
            return format_html('<img src="{}" style="max-height:120px;border-radius:8px;" />', obj.photo.url)
        return "—"
    photo_preview.short_description = "Превью"


# ---------- Case + inline ----------

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 0
    fields = ("kind", "image", "image_preview", "order")
    readonly_fields = ("image_preview",)
    ordering = ("order",)

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="max-height:90px;border-radius:8px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Превью"


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = (CaseImageInline,)

    list_display = ("title", "tag", "duration", "is_active", "order", "updated_at")
    list_filter = ("is_active", "tag")
    search_fields = ("title", "tag", "duration", "description")
    list_editable = ("is_active", "order")
    ordering = ("order",)
    readonly_fields = ("created_at", "updated_at")


# ---------- Review ----------

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author_name", "rating", "is_active", "order", "updated_at")
    list_filter = ("is_active", "rating")
    search_fields = ("author_name", "text")
    list_editable = ("is_active", "order")
    ordering = ("order",)
    readonly_fields = ("created_at", "updated_at")