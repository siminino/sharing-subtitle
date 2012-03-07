from django.contrib.auth.models import User
from django.utils.unittest import TestCase
from django.test.client import Client

from legendas.models import Legenda
from projetos.models import Projeto


class LegendaChangeViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="test", password="test", email="test@test.com")
        self.client = Client()
        self.client.login(username="test", password="test")
        self.projeto = Projeto.objects.create(titulo="Naruto")

    def tearDown(self):
        Legenda.objects.all().delete()
        Projeto.objects.all().delete()
        self.user.delete()

    def test_form_deve_vir_com_instance_de_legenda_relacionado_com_usuario(self):
        response = self.client.get('/admin/legendas/legenda/add/')

        self.assertEquals(200, response.status_code)
        self.assertIn('<p class="readonly">%s</p>' % self.user.username, response.content)

    def test_salvar_legenda_com_sucesso(self):
        data = {'url':u'http://test.com/',
                'projeto': self.projeto.id,
                'episodio': 1}

        response = self.client.post('/admin/legendas/legenda/add/', data)

        self.assertEquals(302, response.status_code)

        legenda = Legenda.objects.filter(projeto=self.projeto, episodio=1)

        self.assertTrue(legenda)
        self.assertEqual(data['url'], legenda[0].url)

    def test_salvar_legenda_com_usuario_logado_relacionado(self):
        data = {'url':u'http://test.com/',
                'projeto': self.projeto.id,
                'episodio': 1}

        self.client.post('/admin/legendas/legenda/add/', data)

        legenda = Legenda.objects.filter(projeto=self.projeto, episodio=1)

        self.assertEqual(self.user, legenda[0].usuario)

