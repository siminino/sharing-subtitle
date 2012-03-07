from django.utils.unittest import TestCase
from django.contrib.auth.models import User

from legendas.models import Legenda
from projetos.models import Projeto
from fansubers.models import Fansub

class LegendaModelTestCase(TestCase):

    def setUp(self):
        self.projeto = Projeto.objects.create(titulo="One Piece")

    def tearDown(self):
        Legenda.objects.all().delete()
        Projeto.objects.all().delete()

    def test_criar_legenda_com_todos_os_campos(self):
        legenda = Legenda.objects.create(url="http://urldownload.com",
                                         projeto=self.projeto,
                                         episodio=1,
                                         raws="zero-raws")

        self.assertEqual(legenda.url, "http://urldownload.com")
        self.assertEqual(legenda.projeto.id, self.projeto.id)
        self.assertEqual(legenda.episodio, 1)
        self.assertEqual(legenda.raws, "zero-raws")

    def test_criar_legenda_com_campos_obrigatorios(self):
        Legenda.objects.create(url="http://urldownload.com",
                               projeto=self.projeto,
                               episodio=1)

        legenda = Legenda.objects.filter(projeto=self.projeto, episodio=1)
        self.assertTrue(legenda)


    def test__unicode__deve_retornar_o_nome_do_projeto_e_o_numero_do_episodio(self):
        legenda = Legenda.objects.create(url="http://urldownload.com",
                                         projeto=self.projeto,
                                         episodio=1,
                                         raws="zero-raws")

        self.assertEquals(legenda.__unicode__(), self.projeto.titulo + ' - %d' % legenda.episodio)


    def test_criar_legenda_relacionada_a_um_fansub(self):
        fansub = Fansub.objects.create(nome="Punch Fansub")
        legenda = Legenda.objects.create(url="http://urldownload.com",
                                         projeto=self.projeto,
                                         episodio=1,
                                         raws="zero-raws",
                                         fansub=fansub)

        self.assertEquals(legenda.fansub, fansub)

    def test_criar_legenda_relacionada_com_usuario(self):
        user = User.objects.create_user(username="test", password="test", email="test@test.com")
        legenda = Legenda.objects.create(url="http://legendaqq.com",
                                         projeto=self.projeto,
                                         episodio=1,
                                         usuario=user)

        self.assertEquals(legenda.usuario, user)
        user.delete()


