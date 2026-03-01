from django.shortcuts import render
from .models import ServicesBanner, Services


def services_page(request):
    banner = ServicesBanner.objects.first()
    services = Services.objects.all()

    context = {
        "bannerServices": banner,
        "services": services,
    }

    return render(request, "services.html", context)