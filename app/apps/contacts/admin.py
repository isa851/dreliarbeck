from django.contrib import admin
from .models import ContactsBanner, ContactsInfo, Booking


@admin.register(ContactsBanner)
class ContactsBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ContactsInfo)
class ContactsInfoAdmin(admin.ModelAdmin):
    list_display = ("addres", "phone")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "phone")
    readonly_fields = ("created_at",)