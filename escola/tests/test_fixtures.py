from django.test import TestCase
from escola.models import Estudante,Curso

class FixtureTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_verifica_carregamento_da_fixture(self):
        """Teste que verifica o carregamento da fixture"""
        estudante = Estudante.objects.get(cpf='04212978245')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular,"80 97788-8088")
        self.assertEqual(curso.codigo,"CPOO1")