from django.db import models
from django.core.urlresolvers import reverse

class DVD(models.Model):
    titulo  = models.CharField(max_length=50)
    genero  = models.CharField(max_length=15)
    ano     = models.IntegerField()
    duracao = models.IntegerField()
    preco   = models.FloatField()

    def get_absolute_url(self):
        return reverse('dvd:detail', kwargs={'pk': self.pk}) 

    def __str__(self):
        ano = str(self.ano)  
        duracao = str(self.duracao)
        return self.titulo + ', ' + self.genero + ', ' + ano + ', ' + duracao