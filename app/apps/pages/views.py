from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json

from apps.pages.models import (
    HomePage,
    ResultsIndex,
    Review,
    DoctorProfile,
    SiteSettings,
    HomeStat,
    ChatBooking,
    Result,
    AboutTheClinic,   # ← ВАЖНО! у тебя его не было
)

from apps.services.models import ServicesHome


# =========================
# INDEX PAGE
# =========================
def index_page(request):
    home = HomePage.objects.order_by("-id").first()
    services_home = ServicesHome.objects.all()

    cases = ResultsIndex.objects.filter(is_active=True).order_by("order")[:6]
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


# =========================
# DOCTOR PAGE
# =========================
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
        "about_the_clinic": about_the_clinic
    })


# =========================
# RESULTS PAGE
# =========================
def results_page(request):
    results = ResultsIndex.objects.filter(is_active=True).order_by("order")
    return render(request, "results.html", {"results": results})


# =========================
# REVIEWS PAGE
# =========================
def reviews_page(request):
    reviews = Review.objects.filter(is_active=True).order_by("order")
    return render(request, "reviews.html", {"reviews": reviews})


# =========================
# CHAT BOOKING API
# =========================
@csrf_exempt   # если пока без CSRF
@require_POST
def chat_booking_api(request):
    try:
        data = json.loads(request.body)

        problem = data.get("problem")
        date = data.get("date")
        fear = data.get("fear")
        name = data.get("name")
        phone = data.get("phone")

        # Базовая валидация
        if not name or not phone:
            return JsonResponse(
                {"success": False, "error": "Имя и телефон обязательны"},
                status=400
            )

        booking = ChatBooking.objects.create(
            problem=problem or "",
            date=date or "",
            fear=fear or "",
            name=name.strip(),
            phone=phone.strip(),
        )

        return JsonResponse({
            "success": True,
            "message": "Заявка успешно сохранена",
            "id": booking.id
        })

    except json.JSONDecodeError:
        return JsonResponse(
            {"success": False, "error": "Некорректный JSON"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e)},
            status=500
        )