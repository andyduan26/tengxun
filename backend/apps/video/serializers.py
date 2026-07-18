from rest_framework import serializers

from .models import VideoProject


class VideoProjectSerializer(serializers.ModelSerializer):
    video_file_url = serializers.SerializerMethodField()

    class Meta:
        model = VideoProject
        fields = [
            "id",
            "title",
            "subtitle",
            "category",
            "tags",
            "cover_image",
            "video_file_url",
            "badge_text",
            "status_text",
            "is_banner",
            "sort_weight",
            "created_at",
            "updated_at",
        ]

    def get_video_file_url(self, obj):
        if not obj.video_file:
            return ""
        request = self.context.get("request")
        url = obj.video_file.url
        if request:
            return request.build_absolute_uri(url)
        return url
