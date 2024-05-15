from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante

class EstudanteTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.client.force_authenticate(user=self.usuario)
        self.url = reverse("Estudantes-list")

        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste de Estudante UM',
            email = 'testeestudante01@gmail.com',
            cpf = '27151855028',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999',
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste de Estudante DOIS',
            email = 'testeestudante02@gmail.com',
            cpf = '99326390012',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999',
        )

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste para verificar a requisição GET para listar os estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        