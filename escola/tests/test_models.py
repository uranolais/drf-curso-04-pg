from escola.models import Estudante, Curso
from django.test import TestCase

class ModelEstudanteTestCase(TestCase):
    
    # def test_falha(self):
    #     self.fail('Teste falhou :(')

    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de Modelo',
            email = 'testemodelo@gmail.com',
            cpf = '70134752031',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999',
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome,'Teste de Modelo')
        self.assertEqual(self.estudante.email,'testemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf,'70134752031')
        self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
        self.assertEqual(self.estudante.celular,'86 99999-9999')