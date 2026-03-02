from django.shortcuts import render
from .models import Cases, CasesBanner


def cases_page(request):
    banner = CasesBanner.objects.first()
    cases = Cases.objects.all()

    context = {
        "banner": banner,
        "cases": cases,
    }
    return render(request, "cases.html", context)