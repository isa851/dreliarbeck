from django.shortcuts import render
from apps.pages.models import HomePage, Service, Case, Review, DoctorProfile

def index_page(request):
    index = HomePage.objects.order_by("-id").first()
    services = Service.objects.filter(is_active=True).order_by("order")
    cases = Case.objects.filter(is_active=True).order_by("order")[:6]
    reviews = Review.objects.filter(is_active=True).order_by("order")[:6]
    doctor = DoctorProfile.objects.order_by("-id").first()

    return render(
        request,
        "index.html",
        {
            "index": index,
            "services": services,
            "cases": cases,
            "reviews": reviews,
            "doctor": doctor,
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
    doctor = DoctorProfile.objects.order_by("-id").first()
    return render(request, "doctor.html", {"doctor": doctor})


def contacts_page(request):
    return render(request, "contacts.html")


def tour_page(request):
    return render(request, "tour.html")