from rest_framework.response import Response
from rest_framework.views import APIView


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
