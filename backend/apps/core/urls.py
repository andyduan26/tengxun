from django.urls import path

from .views import HealthCheckAPIView, HomeBannerListAPIView, HomeRecommendationListAPIView


urlpatterns = [
    path("health/", HealthCheckAPIView.as_view(), name="health-check"),
    path("home/banners/", HomeBannerListAPIView.as_view(), name="home-banners"),
    path(
        "home/recommendations/",
        HomeRecommendationListAPIView.as_view(),
        name="home-recommendations",
    ),
]
