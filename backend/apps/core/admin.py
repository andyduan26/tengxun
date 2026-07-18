import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models import VideoProject


admin.site.site_header = "腾讯视频内容管理后台"
admin.site.site_title = "腾讯视频后台"
admin.site.index_title = "内容运营中心"


@admin.register(VideoProject)
class VideoProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "thumbnail_preview",
        "title",
        "category",
        "is_vip",
        "sort_weight",
        "updated_at",
    )
    list_display_links = ("id", "title")
    list_filter = ("category", "is_vip", "created_at")
    search_fields = ("title", "description", "category")
    readonly_fields = ("cover_preview", "thumbnail_preview", "created_at", "updated_at")
    fieldsets = (
        ("基础信息", {"fields": ("title", "category", "description")}),
        ("图片资源", {"fields": ("cover_image_url", "cover_preview", "thumbnail_url", "thumbnail_preview")}),
        ("运营配置", {"fields": ("is_vip", "sort_weight")}),
        ("系统时间", {"fields": ("created_at", "updated_at")}),
    )
    ordering = ("-sort_weight", "-updated_at")
    list_per_page = 20
    actions = ("mark_as_vip", "mark_as_free", "export_as_csv")

    @admin.display(description="封面预览")
    def cover_preview(self, obj):
        if not obj.cover_image_url:
            return "-"
        return format_html(
            '<img src="{}" style="width: 240px; height: 135px; object-fit: cover;" />',
            obj.cover_image_url,
        )

    @admin.display(description="缩略图")
    def thumbnail_preview(self, obj):
        if not obj.thumbnail_url:
            return "-"
        return format_html(
            '<img src="{}" style="width: 72px; height: 48px; object-fit: cover;" />',
            obj.thumbnail_url,
        )

    @admin.action(description="标记为 VIP")
    def mark_as_vip(self, request, queryset):
        queryset.update(is_vip=True)

    @admin.action(description="标记为免费")
    def mark_as_free(self, request, queryset):
        queryset.update(is_vip=False)

    @admin.action(description="导出所选视频 CSV")
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv; charset=utf-8-sig")
        response["Content-Disposition"] = 'attachment; filename="video_projects.csv"'
        writer = csv.writer(response)
        writer.writerow(["ID", "标题", "分类", "描述/看点", "封面大图 URL", "缩略图 URL", "是否 VIP", "排序权重"])
        for item in queryset:
            writer.writerow(
                [
                    item.id,
                    item.title,
                    item.category,
                    item.description,
                    item.cover_image_url,
                    item.thumbnail_url,
                    "是" if item.is_vip else "否",
                    item.sort_weight,
                ]
            )
        return response
