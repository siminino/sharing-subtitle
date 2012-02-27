from datetime import datetime

from django.utils.unittest import TestCase

from projetos.models import Projeto

class ProjetoModelTestCase(TestCase):

    def tearDown(self):
        Projeto.objects.all().delete()

    def test_criar_projeto_com_todos_os_campos(self):
        projeto = Projeto.objects.create(titulo="Death Note",
                                         total_episodios=37,
                                         genero="Policial, Sobrenatural, Suspense",
                                         estudio="Madhouse",
                                         direcao="Tetsuro Araki",
                                         inicio_exibicao=datetime(year=2006, month=10, day=3),
                                         fim_exibicao=datetime(year=2007, month=6, day=26),
                                         imagem="http://imagemqq"
                                        )

        self.assertEqual(projeto.titulo, "Death Note")
        self.assertEqual(projeto.total_episodios, 37)
        self.assertEqual(projeto.genero,"Policial, Sobrenatural, Suspense")
        self.assertEqual(projeto.estudio, "Madhouse")
        self.assertEqual(projeto.direcao, "Tetsuro Araki")
        self.assertEqual(projeto.inicio_exibicao.strftime("%d/%m/%Y"), "03/10/2006")
        self.assertEqual(projeto.fim_exibicao.strftime("%d/%m/%Y"), "26/06/2007")
        self.assertEqual(projeto.imagem, "http://imagemqq")

    def test_criar_projeto_com_campos_obrigatorios(self):
        Projeto.objects.create(titulo="One Piece")

        projeto = Projeto.objects.filter(titulo="One Piece")
        self.assertTrue(projeto)

    def test__unicode__deve_retornar_titulo_do_projeto(self):
        projeto = Projeto.objects.create(titulo="One Piece")

        self.assertEquals(projeto.titulo, projeto.__unicode__())
