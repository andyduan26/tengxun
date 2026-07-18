from django.contrib import admin
from django.test import TestCase

from .admin import VideoProjectAdmin
from .models import VideoProject


class VideoProjectModelAdminTests(TestCase):
    def test_video_project_has_tencent_video_fields(self):
        project = VideoProject.objects.create(
            title="仙逆",
            subtitle="青宜：只此一次，却真香！",
            category="动漫",
            tags="东方玄幻 东方仙侠 逆袭",
            cover_image="https://example.com/xian-ni.jpg",
            video_file="videos/xian-ni.mp4",
            badge_text="独播",
            status_text="更新至149集",
            is_banner=True,
            sort_weight=100,
        )

        self.assertEqual(str(project), "仙逆")
        self.assertEqual(project.tags, "东方玄幻 东方仙侠 逆袭")
        self.assertEqual(project.video_file.name, "videos/xian-ni.mp4")
        self.assertTrue(project.is_banner)

    def test_video_project_is_registered_in_admin(self):
        model_admin = admin.site._registry[VideoProject]

        self.assertIsInstance(model_admin, VideoProjectAdmin)
        self.assertEqual(
            model_admin.list_display,
            (
                "title",
                "category",
                "is_banner",
                "badge_text",
                "status_text",
                "has_video_file",
                "sort_weight",
                "created_at",
            ),
        )
        self.assertEqual(model_admin.list_filter, ("category", "is_banner", "badge_text"))
