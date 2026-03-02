from django.shortcuts import render
from .models import ReviewBanner, Review, ReviewStats, VideoReview


def review_page(request):
    review_banner = ReviewBanner.objects.first()
    stats = ReviewStats.objects.first()

    text_reviews = Review.objects.all()
    video_reviews = VideoReview.objects.all()

    context = {
        "review_banner": review_banner,
        "stats": stats,
        "text_reviews": text_reviews,
        "video_reviews": video_reviews,
    }

    return render(request, "reviews.html", context)