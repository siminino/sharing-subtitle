from django.utils.unittest import TestCase
from django.contrib import admin

from legendas.models import Legenda


class LegendaAdminTestCase(TestCase):

    def setUp(self):
        import legendas.admin

    def test_legenda_deve_estar_registrado_no_admin_site(self):
        self.assertIn(Legenda, admin.site._registry)
