from django.utils.unittest import TestCase

from fansubers.models import Fansub
from projetos.models import Projeto


class FansubModelTestCase(TestCase):

    def tearDown(self):
        Fansub.objects.all().delete()
        Projeto.objects.all().delete()

    def test_criar_fansub_com_todos_os_campos(self):
        fansub = Fansub.objects.create(nome="Punch Fansub",
                                       site="http://punchfansub.com")

        self.assertEquals(fansub.nome, "Punch Fansub")
        self.assertEquals(fansub.site, "http://punchfansub.com")

    def test_criar_fansub_com_campos_obrigatorios(self):
        Fansub.objects.create(nome="Punch Fansub")

        fansub = Fansub.objects.filter(nome="Punch Fansub")
        self.assertTrue(fansub)

    def test_relacionar_fansub_com_projetos(self):
        projeto = Projeto.objects.create(titulo="One Piece")
        fansub = Fansub.objects.create(nome="Punch Fansub")
        fansub.projetos.add(projeto)
        fansub.save()

        fansub = Fansub.objects.get(id=fansub.id)
        self.assertIn(projeto, fansub.projetos.all())

    def test__unicode__deve_retornar_nome_do_fansub(self):
        fansub = Fansub.objects.create(nome="Punch Fansub")
        self.assertEquals(fansub.nome, fansub.__unicode__())
