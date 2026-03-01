from django.shortcuts import render
from apps.pages.models import (
    HomePage,
    Case,
    Review,
    DoctorProfile,
    SiteSettings,
    HomeStat,
    Result,
)
from apps.services.models import ServicesHome


def index_page(request):
    home = HomePage.objects.order_by("-id").first()

    services_home = ServicesHome.objects.all()

    cases = Case.objects.filter(is_active=True).order_by("order")[:6]
    reviews = Review.objects.filter(is_active=True).order_by("order")[:6]
    results = Result.objects.order_by("-id")
    doctors = DoctorProfile.objects.all()[:4]
    settings = SiteSettings.objects.order_by("-id").first()
    stats = HomeStat.objects.filter(home=home).order_by("order") if home else []

    context = {
        "index": home,
        "services_home": services_home,
        "cases": cases,
        "reviews": reviews,
        "doctors": doctors,
        "settings": settings,
        "stats": stats,
        "results": results,
    }

    return render(request, "index.html", context)

def doctor_page(request):
    about_the_clinic = (
        AboutTheClinic.objects
        .prefetch_related(
            "philosophies",
            "interiors",
            "certificates",
        )
        .order_by("-id")
        .first()
    )

    return render(request, "doctor.html", {
        # "index": index,
        "about_the_clinic": about_the_clinic
    })

def cases_page(request):
    cases = Case.objects.filter(is_active=True).order_by("order")
    return render(request, "cases.html", {"cases": cases})


def reviews_page(request):
    reviews = Review.objects.filter(is_active=True).order_by("order")
    return render(request, "reviews.html", {"reviews": reviews})


def contacts_page(request):
    return render(request, "contacts.html")


def tour_page(request):
    return render(request, "tour.html")