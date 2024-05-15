from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='lais',password='lais')
        self.client.force_authenticate(user=self.usuario)