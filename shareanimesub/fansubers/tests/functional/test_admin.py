from django.utils.unittest import TestCase
from django.contrib import admin

from fansubers.models import Fansub

class FansubAdminTestCase(TestCase):

    def setUp(self):
        import fansubers.admin

    def test_Fansub_deve_estar_registrado_no_admin(self):
        self.assertIn(Fansub, admin.site._registry)
