from django.contrib import admin
from apps.pages.models import (
    SiteSettings, HomePage, HomeStat, HomeFeature,
    DoctorProfile,
    Case, CaseImage,
    Review,
    Result,
    AboutTheClinic,
    Philosophy,
    Interior,
    Certificates,
)

admin.site.register(SiteSettings)
admin.site.register(HomePage)
admin.site.register(HomeStat)
admin.site.register(HomeFeature)
admin.site.register(Result)

admin.site.register(AboutTheClinic)
admin.site.register(Philosophy)
admin.site.register(Interior)
admin.site.register(Certificates)
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    fields = ("name", "role", "description", "photo")
admin.site.register(Case)
admin.site.register(CaseImage)
admin.site.register(Review)