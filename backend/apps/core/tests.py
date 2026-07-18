from django.test import TestCase
from django.urls import reverse

from .models import VideoProject


class HealthCheckAPITests(TestCase):
    def test_health_check_returns_standard_json(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "success": True,
                "data": {
                    "status": "ok",
                    "service": "backend",
                },
                "message": "Backend is healthy",
            },
        )


class HomeVideoProjectAPITests(TestCase):
    def setUp(self):
        categories = [
            ("仙逆", "动漫", 100),
            ("脱口秀3", "综艺", 90),
            ("繁花", "电视剧", 80),
            ("流浪地球", "电影", 70),
            ("庆余年", "电视剧", 60),
            ("长相思", "电视剧", 50),
        ]
        for title, category, sort_weight in categories:
            VideoProject.objects.create(
                title=title,
                description=f"{title} 看点",
                cover_image_url=f"https://example.com/{title}/cover.jpg",
                thumbnail_url=f"https://example.com/{title}/thumb.jpg",
                category=category,
                is_vip=sort_weight >= 80,
                sort_weight=sort_weight,
            )

    def test_home_banners_returns_latest_five_by_weight(self):
        response = self.client.get(reverse("home-banners"))

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["success"])
        self.assertEqual(len(payload["data"]), 5)
        self.assertEqual(
            [item["title"] for item in payload["data"]],
            ["仙逆", "脱口秀3", "繁花", "流浪地球", "庆余年"],
        )

    def test_home_recommendations_filters_by_category(self):
        response = self.client.get(reverse("home-recommendations"), {"category": "电视剧"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["success"])
        self.assertEqual(
            [item["title"] for item in payload["data"]],
            ["繁花", "庆余年", "长相思"],
        )

    def test_home_recommendations_all_returns_all_categories(self):
        response = self.client.get(reverse("home-recommendations"), {"category": "全部"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 6)
