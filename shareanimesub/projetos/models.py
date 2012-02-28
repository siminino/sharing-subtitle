from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    total_episodios = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=70, blank=True, null=True)
    estudio = models.CharField(max_length=50, blank=True, null=True)
    direcao = models.CharField(max_length=50, blank=True, null=True)
    inicio_exibicao = models.DateField(blank=True, null=True)
    fim_exibicao = models.DateField(blank=True, null=True)
    imagem = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo

