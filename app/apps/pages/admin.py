from django.contrib import admin
from apps.pages.models import (
    SiteSettings, HomePage, HomeStat, HomeFeature,
    Service,
    DoctorProfile,
    Case, CaseImage,
    Review,
)

admin.site.register(SiteSettings)
admin.site.register(HomePage)
admin.site.register(HomeStat)
admin.site.register(HomeFeature)
admin.site.register(Service)

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    fields = ("name", "role", "description", "photo")
admin.site.register(Case)
admin.site.register(CaseImage)
admin.site.register(Review)