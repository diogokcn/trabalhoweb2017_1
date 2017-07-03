
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class Livro(models.Model):
    titulo  = models.CharField(verbose_name=_(u'Título'), max_length=100)
    ano     = models.IntegerField(verbose_name=_('Ano'))
    editora = models.CharField(verbose_name=_('Editora'), max_length=20)
    autora  = models.CharField(verbose_name=_('Autora'),  max_length=30)
    nroPags = models.IntegerField(verbose_name=_(u'Nro Páginas'))
    formato = models.CharField(verbose_name=_('Formato'), max_length=20)
    preco   = models.FloatField(verbose_name=_(u'Preço'))
    
    def get_absolute_url(self):
        return reverse('livro:detail', kwargs={'pk': self.pk}) 

    def __str__(self):
        ano = str(self.ano)  
        return self.titulo + ', ' + self.autora + ', ' + ano + ', ' + self.editora
