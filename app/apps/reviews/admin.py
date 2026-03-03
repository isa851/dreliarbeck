from django.contrib import admin
from .models import Review, ReviewBanner, VideoReview, ReviewStats


@admin.register(ReviewStats)
class ReviewStatsAdmin(admin.ModelAdmin):
    list_display = ("patients", "average_rating", "recommend")
    search_fields = ("patients",)


@admin.register(VideoReview)
class VideoReviewAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(ReviewBanner)
class ReviewBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "text_rating", "time")
    list_filter = ("time",)
    search_fields = ("author",)