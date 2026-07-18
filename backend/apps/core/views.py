from rest_framework.response import Response
from rest_framework.views import APIView

from apps.video.models import VideoProject
from apps.video.serializers import VideoProjectSerializer


class HealthCheckAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(
            {
                "success": True,
                "data": {
                    "status": "ok",
                    "service": "backend",
                },
                "message": "Backend is healthy",
            }
        )


class HomeBannerListAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        projects = VideoProject.objects.filter(is_banner=True)[:5]
        serializer = VideoProjectSerializer(projects, many=True)
        return Response(
            {
                "success": True,
                "data": serializer.data,
                "message": "Home banners loaded",
            }
        )


class HomeRecommendationListAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        category = request.query_params.get("category", "全部")
        projects = VideoProject.objects.all()
        if category and category != "全部":
            projects = projects.filter(category=category)

        serializer = VideoProjectSerializer(projects, many=True)
        return Response(
            {
                "success": True,
                "data": serializer.data,
                "message": "Home recommendations loaded",
            }
        )
