from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ContactsBanner, ContactsInfo, Booking


def contacts_page(request):
    contacts_banner = ContactsBanner.objects.first()
    contacts_info = ContactsInfo.objects.first()

    return render(request, "contacts.html", {
        "contacts_banner": contacts_banner,
        "contacts_info": contacts_info,
    })


@csrf_exempt
def booking_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            name = data.get("name")
            phone = data.get("phone")
            service = data.get("service")
            comment = data.get("comment")

            if not name or not phone:
                return JsonResponse({"success": False, "error": "Имя и телефон обязательны"}, status=400)

            Booking.objects.create(
                name=name,
                phone=phone,
                service=service,
                comment=comment,
            )

            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False}, status=405)