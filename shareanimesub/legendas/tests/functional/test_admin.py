from django.utils.unittest import TestCase
from django.contrib import admin

from legendas.models import Legenda
from legendas.admin import LegendaAdmin


class LegendaAdminTestCase(TestCase):

    def setUp(self):
        import legendas.admin

    def test_legenda_deve_estar_registrado_no_admin_site(self):
        self.assertIn(Legenda, admin.site._registry)

    def test_admin_deve_conter_classe_LegendaAdmin(self):
        self.assertEquals(LegendaAdmin, admin.site._registry[Legenda].__class__)

    def test_legenda_admin_deve_conter_list_filter_de_projeto(self):
        self.assertIn('projeto', LegendaAdmin.list_filter)

    def test_legenda_admin_deve_conter_list_filter_de_fansub(self):
        self.assertIn('fansub', LegendaAdmin.list_filter)

    def test_LegendaAdmin_deve_ordenar_por_episodio(self):
        self.assertIn('episodio', LegendaAdmin.ordering)


