from .models import SiteSettings

def site_settings(request):
    obj = SiteSettings.objects.order_by("-id").first()
    return {"site_settings": obj}