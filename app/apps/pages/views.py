from django.shortcuts import render
from apps.pages.models import (
    HomePage,
    Service,
    Case,
    Review,
    DoctorProfile,
    SiteSettings,
    HomeStat,
    Result,
)


def index_page(request):
    index = HomePage.objects.order_by("-id").first()

    services = Service.objects.filter(is_active=True).order_by("order")
    cases = Case.objects.filter(is_active=True).order_by("order")[:6]
    reviews = Review.objects.filter(is_active=True).order_by("order")[:6]

    results = Result.objects.order_by("order")
    doctors = DoctorProfile.objects.order_by("-id")[:4]

    results = Result.objects.order_by("-id")     
    settings = SiteSettings.objects.order_by("-id").first()

    stats = HomeStat.objects.filter(home=index).order_by("order") if index else []

    return render(
        request,
        "index.html",
        {
            "index": index,
            "services": services,
            "cases": cases,
            "reviews": reviews,

            "doctor": doctors,     
            "doctors": doctors,    

            "settings": settings,
            "stats": stats,
            "results": results,
        },
    )


def services_page(request):
    services = Service.objects.filter(is_active=True).order_by("order")
    return render(request, "services.html", {"services": services})


def cases_page(request):
    cases = Case.objects.filter(is_active=True).order_by("order")
    return render(request, "cases.html", {"cases": cases})


def reviews_page(request):
    reviews = Review.objects.filter(is_active=True).order_by("order")
    return render(request, "reviews.html", {"reviews": reviews})


def doctor_page(request):
    doctors = DoctorProfile.objects.order_by("-id")
    return render(request, "doctor.html", {"doctors": doctors})


def contacts_page(request):
    return render(request, "contacts.html")


def tour_page(request):
    return render(request, "tour.html")