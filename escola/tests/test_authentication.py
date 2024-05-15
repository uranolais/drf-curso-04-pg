from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.usuario = User.objects.create_superuser(username='lais',password='lais')
        self.url = reverse("Estudantes-list")
    
    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        usuario = authenticate(username = 'lais', password = 'lais')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um user com o username incorreto"""
        usuario = authenticate(username='las',password = 'lais')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_user_com_password_incorreto(self):
        """Teste que verifica a autenticação de um user com o password incorreto"""
        usuario = authenticate(username='lais',password = 'las')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Teste que verifica uma requisição GET autorizada (user autenticado)"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada (user não autenticado)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)