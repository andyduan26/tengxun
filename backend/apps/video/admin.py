from django.contrib import admin
from django.utils.html import format_html

from .models import VideoProject


@admin.register(VideoProject)
class VideoProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_banner",
        "badge_text",
        "status_text",
        "has_video_file",
        "sort_weight",
        "created_at",
    )
    list_filter = ("category", "is_banner", "badge_text")
    search_fields = ("title", "subtitle", "tags")
    ordering = ("-sort_weight",)
    readonly_fields = ("cover_preview", "created_at", "updated_at")
    list_per_page = 20
    fieldsets = (
        ("基础信息", {"fields": ("title", "subtitle", "category", "tags")}),
        ("视觉资源", {"fields": ("cover_image", "cover_preview")}),
        ("视频文件", {"fields": ("video_file",)}),
        ("运营配置", {"fields": ("badge_text", "status_text", "is_banner", "sort_weight")}),
        ("系统时间", {"fields": ("created_at", "updated_at")}),
    )

    @admin.display(description="横版封面预览")
    def cover_preview(self, obj):
        if not obj.cover_image:
            return "-"
        return format_html(
            '<img src="{}" style="width: 280px; height: 158px; object-fit: cover;" />',
            obj.cover_image,
        )

    @admin.display(description="视频文件", boolean=True)
    def has_video_file(self, obj):
        return bool(obj.video_file)
