from django.db import models

from django.contrib.auth.models import User

from projetos.models import Projeto
from fansubers.models import Fansub

class Legenda(models.Model):
    url = models.URLField()
    projeto = models.ForeignKey(Projeto)
    episodio = models.IntegerField()
    raws = models.CharField(max_length=255, blank=True, null=True)
    fansub = models.ForeignKey(Fansub, blank=True, null=True)
    usuario = models.ForeignKey(User, verbose_name="Atualizado por", blank=True, null=True)

    def __unicode__(self):
        return self.projeto.titulo + ' - %d' % self.episodio

