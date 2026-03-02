from django.contrib import admin
from .models import ContactsBanner, ContactsInfo, Booking


admin.site.register(ContactsBanner)
admin.site.register(ContactsInfo)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "phone")