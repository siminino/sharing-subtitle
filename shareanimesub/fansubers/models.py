from django.db import models

from projetos.models import Projeto


class Fansub(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField(blank=True, null=True)
    projetos = models.ManyToManyField(Projeto)

    def __unicode__(self):
        return self.nome

