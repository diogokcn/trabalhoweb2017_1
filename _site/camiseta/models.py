
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class Camiseta(models.Model):
    marca   = models.CharField(verbose_name=_('Marca'),   max_length=20)
    tamanho = models.CharField(verbose_name=_('Tamanho'), max_length=10)
    cor     = models.CharField(verbose_name=_('Cor'), 	  max_length=10)
    tecido  = models.CharField(verbose_name=_('Tecido'),  max_length=30)   
    preco   = models.FloatField(verbose_name=_(u'Preço'))

    def get_absolute_url(self):
        return reverse('camiseta:detail', kwargs={'pk': self.pk}) 

    def __str__(self):
        return self.marca + ', ' + self.tamanho + ', ' + self.cor + ', ' + self.tecido