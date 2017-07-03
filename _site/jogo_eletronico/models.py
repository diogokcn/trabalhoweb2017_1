
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class JogoEletronico(models.Model):
    titulo       = models.CharField(verbose_name=_(u'Título'),       max_length=50)
    estudio      = models.CharField(verbose_name=_(u'Estúdio'),      max_length=20)
    distribuidor = models.CharField(verbose_name=_(u'Distribuidor'), max_length=20)
    genero       = models.CharField(verbose_name=_(u'Gênero'),       max_length=20)
    ano          = models.IntegerField(verbose_name=_('Ano'))
    preco        = models.FloatField(verbose_name=_(u'Preço'))

    def get_absolute_url(self):
    	return reverse('jogo:detail', kwargs={'pk': self.pk})


    def __str__(self):
    	ano = str(self.ano)
    	return self.titulo