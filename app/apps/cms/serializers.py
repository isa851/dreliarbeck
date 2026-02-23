from rest_framework import serializers

from .models import (
    SiteSettings,
    HomePage, HomeStat, HomeFeature,
    Service,
    DoctorProfile, DoctorFact,
    Case, CaseImage,
    Review,
)


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



class HomeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStat
        fields = ("id", "value", "label", "order")


class HomeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFeature
        fields = ("id", "title", "text", "icon", "order")


class HomePageSerializer(serializers.ModelSerializer):
    stats = HomeStatSerializer(many=True, required=False)
    features = HomeFeatureSerializer(many=True, required=False)

    class Meta:
        model = HomePage
        fields = (
            "id",
            "hero_badge",
            "hero_title",
            "hero_subtitle",
            "hero_bg",
            "cta_primary_text",
            "cta_primary_url",
            "cta_secondary_text",
            "cta_secondary_url",
            "trust_title",
            "trust_subtitle",
            "services_title",
            "services_subtitle",
            "services_all_url",
            "tour_title",
            "tour_subtitle",
            "tour_image",
            "tour_url",
            "final_cta_title",
            "final_cta_text",
            "final_cta_primary_text",
            "final_cta_primary_url",
            "final_cta_secondary_text",
            "final_cta_secondary_url",
            "created_at",
            "updated_at",
            "stats",
            "features",
        )

    def create(self, validated_data):
        stats_data = validated_data.pop("stats", [])
        features_data = validated_data.pop("features", [])

        home = HomePage.objects.create(**validated_data)

        for item in stats_data:
            HomeStat.objects.create(home=home, **item)

        for item in features_data:
            HomeFeature.objects.create(home=home, **item)

        return home

    def update(self, instance, validated_data):
        stats_data = validated_data.pop("stats", None)
        features_data = validated_data.pop("features", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if stats_data is not None:
            instance.stats.all().delete()
            for item in stats_data:
                HomeStat.objects.create(home=instance, **item)

        if features_data is not None:
            instance.features.all().delete()
            for item in features_data:
                HomeFeature.objects.create(home=instance, **item)

        return instance



class DoctorFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorFact
        fields = ("id", "text", "icon", "order")


class DoctorProfileSerializer(serializers.ModelSerializer):
    facts = DoctorFactSerializer(many=True, required=False)

    class Meta:
        model = DoctorProfile
        fields = (
            "id",
            "name",
            "role",
            "specialty",
            "description",
            "photo",
            "details_url",
            "created_at",
            "updated_at",
            "facts",
        )

    def create(self, validated_data):
        facts_data = validated_data.pop("facts", [])
        doctor = DoctorProfile.objects.create(**validated_data)

        for item in facts_data:
            DoctorFact.objects.create(doctor=doctor, **item)

        return doctor

    def update(self, instance, validated_data):
        facts_data = validated_data.pop("facts", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if facts_data is not None:
            instance.facts.all().delete()
            for item in facts_data:
                DoctorFact.objects.create(doctor=instance, **item)

        return instance




class CaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseImage
        fields = ("id", "kind", "image", "order")


class CaseSerializer(serializers.ModelSerializer):
    images = CaseImageSerializer(many=True, required=False)

    class Meta:
        model = Case
        fields = (
            "id",
            "tag",
            "duration",
            "title",
            "description",
            "is_active",
            "order",
            "created_at",
            "updated_at",
            "images",
        )

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        case = Case.objects.create(**validated_data)

        for item in images_data:
            CaseImage.objects.create(case=case, **item)

        return case

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            instance.images.all().delete()
            for item in images_data:
                CaseImage.objects.create(case=instance, **item)

        return instance