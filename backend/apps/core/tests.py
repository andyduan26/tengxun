from django.test import TestCase
from django.urls import reverse


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
