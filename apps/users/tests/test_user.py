from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        response = self.client.post('/api/auth/users/', {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'role': 'CLIENTE',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
