from rest_framework.routers import DefaultRouter
from .views import (
    SiteSettingsViewSet,
    HomePageViewSet,
    ServiceViewSet,
    DoctorProfileViewSet,
    CaseViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r"site-settings", SiteSettingsViewSet, basename="site-settings")
router.register(r"home-page", HomePageViewSet, basename="home-page")
router.register(r"services", ServiceViewSet, basename="services")
router.register(r"doctors", DoctorProfileViewSet, basename="doctors")
router.register(r"cases", CaseViewSet, basename="cases")
router.register(r"reviews", ReviewViewSet, basename="reviews")

urlpatterns = router.urls