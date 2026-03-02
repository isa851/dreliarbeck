from django.shortcuts import render
from apps.tur.models import TurBanner, TurClinik


def tur_view(request):
    tur_banner = TurBanner.objects.order_by('-id').first()
    tur_clinik = TurClinik.objects.all()

    context = {
        'tur_banner': tur_banner,
        'tur_clinik': tur_clinik,
    }

    return render(request, 'tour.html', context)