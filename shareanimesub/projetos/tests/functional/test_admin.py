from django.utils.unittest import TestCase
from django.contrib import admin

from projetos.models import Projeto

class ProjetoAdminTestCase(TestCase):

    def setUp(self):
        import projetos.admin

    def test_Projeto_deve_estar_registrado(self):
        self.assertIn(Projeto, admin.site._registry)
