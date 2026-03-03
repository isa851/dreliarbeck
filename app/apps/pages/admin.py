from django.contrib import admin
from .models import (
    SiteSettings,
    HomePage,
    HomeStat,
    HomeFeature,
    DoctorProfile,
    ResultsIndex,
    ResultsIndexImage,
    Review,
    Result,
    AboutTheClinic,
    Philosophy,
    Interior,
    Certificates,
    ChatBooking,
)

# ================================
# SITE SETTINGS (только одна запись)
# ================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("phone", "address")

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True


# ================================
# HOME PAGE
# ================================

class HomeStatInline(admin.TabularInline):
    model = HomeStat
    extra = 1


class HomeFeatureInline(admin.TabularInline):
    model = HomeFeature
    extra = 1


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "created_at")
    inlines = [HomeStatInline, HomeFeatureInline]


# ================================
# DOCTOR
# ================================

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "created_at")
    search_fields = ("name", "role")


# ================================
# RESULTS (КЕЙСЫ)
# ================================

class ResultsImageInline(admin.TabularInline):
    model = ResultsIndexImage
    extra = 1


@admin.register(ResultsIndex)
class ResultsIndexAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "duration", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "tag")
    ordering = ("order",)
    inlines = [ResultsImageInline]


# ================================
# RESULT (одиночные результаты)
# ================================

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "order")
    list_editable = ("order",)
    search_fields = ("title", "type")


# ================================
# REVIEWS
# ================================

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author_name", "rating", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active", "rating")
    search_fields = ("author_name",)


# ================================
# ABOUT THE CLINIC
# ================================

class PhilosophyInline(admin.TabularInline):
    model = Philosophy
    extra = 1


class InteriorInline(admin.TabularInline):
    model = Interior
    extra = 1


class CertificatesInline(admin.TabularInline):
    model = Certificates
    extra = 1


@admin.register(AboutTheClinic)
class AboutTheClinicAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    inlines = [PhilosophyInline, InteriorInline, CertificatesInline]


# ================================
# CHAT BOOKING
# ================================

@admin.register(ChatBooking)
class ChatBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "problem", "date", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "problem")
    readonly_fields = ("created_at",)