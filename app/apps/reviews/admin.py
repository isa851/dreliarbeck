from django.contrib import admin


from apps.reviews.models import Review,ReviewBanner


@admin.register(ReviewBanner)
class ReviewBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    search_fields = ["title", "description"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author", "text_rating", "time"]
    search_fields = ["author", "text_rating", "time"]
    list_filter = ["time"]
    
