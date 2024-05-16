from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudanteTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        #self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.usuario = User.objects.get(username = 'lais')
        self.client.force_authenticate(user=self.usuario)
        self.url = reverse("Estudantes-list") #/estudantes/

        # self.estudante_01 = Estudante.objects.create(
        #     nome = 'Teste de Estudante UM',
        #     email = 'testeestudante01@gmail.com',
        #     cpf = '27151855028',
        #     data_nascimento = '2023-02-02',
        #     celular = '86 99999-9999',
        # )
        self.estudante_01 = Estudante.objects.get(pk=1)
        # self.estudante_02 = Estudante.objects.create(
        #     nome = 'Teste de Estudante DOIS',
        #     email = 'testeestudante02@gmail.com',
        #     cpf = '99326390012',
        #     data_nascimento = '2023-02-02',
        #     celular = '86 99999-9999',
        # )
        self.estudante_02 = Estudante.objects.get(pk=2)
        

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste para verificar a requisição GET para listar os estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_um_estudante(self):
        """Teste para verificar a requisição GET para listar um estudante"""
        #/estudantes/1/
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        # print(dados_estudante_serializados)
        self.assertEqual(response.data,dados_estudante_serializados)

    def test_requisicao_post_para_criar_estudante(self):
        """Teste para verificar a requisição POST para criar um estudante"""
        dados = {
            "nome":"Teste",
            "email":"teste03@gmail.com",
            "cpf":"05408542041",
            "data_nascimento":"2003-04-05",
            "celular":"11 99999-9999"
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_estudante(self):
        """Teste para verificar a requisição DELETE para deletar um estudante"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_estudante(self):
        """Teste para verificar a requisição PUT para atualizar um estudante"""
        dados = {
            'nome':'Teste',
            'email':'testeum@gmail.com',
            'cpf':'82271917034',
            'data_nascimento':'2003-02-02',
            'celular':'66 95984-7070'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        