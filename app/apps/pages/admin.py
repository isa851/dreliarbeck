from django.contrib import admin
from apps.pages.models import (
    SiteSettings, HomePage, HomeStat, HomeFeature,
    DoctorProfile,
    ResultsIndex, ResultsIndexImage,
    Review,
    Result,
    AboutTheClinic,
    Philosophy,
    Interior,
    Certificates,
    ChatBooking,
)


@admin.register(ChatBooking)
class ChatBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "problem", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone")

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
admin.site.register(ResultsIndex)
admin.site.register(ResultsIndexImage)
admin.site.register(Review)