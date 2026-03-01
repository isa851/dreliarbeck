from django.shortcuts import render
from .models import (
    AboutTheClinicBanner,
    AboutTheClinicDoctor,
    AboutTheClinicOurTeam,
    AboutTheClinicPhilosophy,
    AboutTheClinicInterior,
    AboutTheClinicCertificates
)

def about_the_clinic_page(request):
    banner = AboutTheClinicBanner.objects.first()
    doctor = AboutTheClinicDoctor.objects.first()
    team = AboutTheClinicOurTeam.objects.all()
    philosophy = AboutTheClinicPhilosophy.objects.all()
    interior = AboutTheClinicInterior.objects.all()
    certificates = AboutTheClinicCertificates.objects.all()

    context = {
        "banner": banner,
        "doctor": doctor,
        "team": team,
        "philosophy": philosophy,
        "interior": interior,
        "certificates": certificates,
    }

    return render(request, "doctor.html", context)