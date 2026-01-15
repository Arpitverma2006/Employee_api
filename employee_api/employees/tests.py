from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class EmployeeAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="test123"
        )
        response = self.client.post('/api/token/', {
            "username": "test",
            "password": "test123"
        })
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access']
        )

    def test_create_employee(self):
        data = {
            "name": "Ajay",
            "email": "ajay@test.com",
            "department": "Engineering"
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
