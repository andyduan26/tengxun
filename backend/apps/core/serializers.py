from rest_framework import serializers

from .models import VideoProject


class VideoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProject
        fields = [
            "id",
            "title",
            "description",
            "cover_image_url",
            "thumbnail_url",
            "category",
            "is_vip",
            "sort_weight",
            "created_at",
            "updated_at",
        ]
