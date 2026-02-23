from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    SiteSettings,
    HomePage,
    Service,
    DoctorProfile,
    Case,
    Review,
)

from .serializers import (
    SiteSettingsSerializer,
    HomePageSerializer,
    ServiceSerializer,
    DoctorProfileSerializer,
    CaseSerializer,
    ReviewSerializer,
)


class ReadOnlyOrAdminWritePermission(BasePermission):
    """
    SAFE_METHODS (GET/HEAD/OPTIONS) - всем
    Любые записи/изменения (POST/PUT/PATCH/DELETE) - только авторизованным
    (Если хочешь именно админов — ниже покажу как)
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Чтобы DRF не падал при object-level проверках
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyOrAdminWritePermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


class SiteSettingsViewSet(BaseViewSet):
    queryset = SiteSettings.objects.all().order_by("-id")
    serializer_class = SiteSettingsSerializer


class HomePageViewSet(BaseViewSet):
    queryset = HomePage.objects.all().order_by("-id")
    serializer_class = HomePageSerializer


class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    filterset_fields = ["is_active"]
    search_fields = ["title", "description"]
    ordering_fields = ["order", "created_at", "price_from"]


class DoctorProfileViewSet(BaseViewSet):
    queryset = DoctorProfile.objects.all().order_by("-id")
    serializer_class = DoctorProfileSerializer

    search_fields = ["name", "role", "specialty", "description"]
    ordering_fields = ["created_at", "updated_at"]


class CaseViewSet(BaseViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    filterset_fields = ["is_active", "tag"]
    search_fields = ["title", "description", "tag"]
    ordering_fields = ["order", "created_at", "updated_at"]


class ReviewViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    filterset_fields = ["is_active", "rating"]
    search_fields = ["text", "author_name"]
    ordering_fields = ["order", "created_at", "rating"]