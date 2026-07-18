from django.test import TestCase
from django.urls import reverse
from django.contrib import admin

from .admin import VideoProjectAdmin as CoreVideoProjectAdmin
from .models import VideoProject as CoreVideoProject
from apps.video.models import VideoProject


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
            ("仙逆", "动漫", True, 100),
            ("脱口秀3", "综艺", True, 90),
            ("繁花", "电视剧", True, 80),
            ("流浪地球", "电影", True, 70),
            ("庆余年", "电视剧", True, 60),
            ("长相思", "电视剧", False, 50),
        ]
        for title, category, is_banner, sort_weight in categories:
            VideoProject.objects.create(
                title=title,
                subtitle=f"{title} 看点",
                category=category,
                tags=f"{category} 热门 推荐",
                cover_image=f"https://example.com/{title}/cover.jpg",
                badge_text="VIP" if sort_weight >= 80 else "",
                status_text="更新中",
                is_banner=is_banner,
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
        self.assertIn("subtitle", payload["data"][0])
        self.assertIn("badge_text", payload["data"][0])
        self.assertIn("status_text", payload["data"][0])

    def test_home_banners_filters_by_category(self):
        response = self.client.get(reverse("home-banners"), {"category": "电影"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["success"])
        self.assertEqual([item["title"] for item in payload["data"]], ["流浪地球"])

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


class VideoProjectAdminTests(TestCase):
    def test_video_project_admin_has_management_features(self):
        model_admin = admin.site._registry[CoreVideoProject]

        self.assertIsInstance(model_admin, CoreVideoProjectAdmin)
        self.assertIn("cover_preview", model_admin.readonly_fields)
        self.assertIn("export_as_csv", model_admin.actions)
        self.assertEqual(admin.site.site_header, "腾讯视频内容管理后台")
