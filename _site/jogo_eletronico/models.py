from django.db import models
from django.core.urlresolvers import reverse


class JogoEletronico(models.Model):
    titulo       = models.CharField(max_length=50)
    estudio      = models.CharField(max_length=20)
    distribuidor = models.CharField(max_length=20)
    genero       = models.CharField(max_length=20)
    ano          = models.IntegerField()
    preco        = models.FloatField()

    def get_absolute_url(self):
    	return reverse('jogo:detail', kwargs={'pk': self.pk})


    def __str__(self):
    	ano = str(self.ano)
    	return self.titulo