from rest_framework import serializers

from .models import VideoProject


class VideoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProject
        fields = [
            "id",
            "title",
            "subtitle",
            "category",
            "tags",
            "cover_image",
            "badge_text",
            "status_text",
            "is_banner",
            "sort_weight",
            "created_at",
            "updated_at",
        ]
