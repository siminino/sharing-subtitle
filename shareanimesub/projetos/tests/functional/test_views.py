# -*- coding: utf-8 -*-
from django.utils.unittest import TestCase
from django.test.client import RequestFactory, Client

from projetos.models import Projeto
from projetos.views import pagina_projeto

class ProjetoViewTestCase(TestCase):

    def setUp(self):
        self.projeto = Projeto.objects.create(titulo="Full Metal Alchemist: Brotherhood ",
                                              total_episodios=64,
                                              genero="Shonen, Ação, Aventura, Drama, Steampunk",
                                              estudio="Bones/Aniplex",
                                              direcao="Yasuhiro Irie",
                                              inicio_exibicao="2009-04-05",
                                              fim_exibicao="2010-07-04",
                                              imagem="http://imagem.com")
        self.factory = RequestFactory()
        self.request = self.factory.get('/projeto/%d/' % self.projeto.id)
        self.response = pagina_projeto(self.request, self.projeto.id)

    def tearDown(self):
        self.projeto.delete()

    def test_deve_retornar_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_deve_retornar_se_projeto_for_invalido(self):
        try:
            pagina_projeto(self.request, 2000)
        except:
            assert True
            return
        assert False

    def test_deve_retornar_projeto_no_contexto(self):
        self.assertEqual(self.projeto, self.response.context_data['projeto'])

    def test_deve_retornar_template_esperado(self):
        self.assertEqual('projetos/projeto.html', self.response.template_name)

    def test_url_deve_retornar_200(self):
        try:
            response = Client().get("/projeto/%d/" % self.projeto.id)
        except:
            assert False

        self.assertEquals(200, response.status_code)
