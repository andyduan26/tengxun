from django.contrib import admin

from .models import VideoProject


@admin.register(VideoProject)
class VideoProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "is_vip", "sort_weight", "created_at")
    list_filter = ("category", "is_vip", "created_at")
    search_fields = ("title", "description", "category")
    ordering = ("-sort_weight", "-created_at")
    list_per_page = 20
    actions = ("mark_as_vip", "mark_as_free")

    @admin.action(description="标记为 VIP")
    def mark_as_vip(self, request, queryset):
        queryset.update(is_vip=True)

    @admin.action(description="标记为免费")
    def mark_as_free(self, request, queryset):
        queryset.update(is_vip=False)
