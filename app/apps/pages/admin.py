from django.contrib import admin
from .models import (
    SiteSettings,
    HomePage, HomeStat, HomeFeature,
    Service,
    DoctorProfile, DoctorFact,
    Case, CaseImage,
    Review,
)

class HomeStatInline(admin.TabularInline):
    model = HomeStat
    extra = 0

class HomeFeatureInline(admin.TabularInline):
    model = HomeFeature
    extra = 0

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [HomeStatInline, HomeFeatureInline]

class DoctorFactInline(admin.TabularInline):
    model = DoctorFact
    extra = 0

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    inlines = [DoctorFactInline]

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 0

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseImageInline]
    list_display = ("title", "tag", "is_active", "order")
    list_filter = ("is_active", "tag")
    search_fields = ("title", "description", "tag")

admin.site.register(SiteSettings)
admin.site.register(Service)
admin.site.register(Review)