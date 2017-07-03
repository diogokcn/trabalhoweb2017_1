
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

class DVD(models.Model):
    titulo  = models.CharField(verbose_name=_(u'Título'), max_length=50)
    genero  = models.CharField(verbose_name=_(u'Gênero'), max_length=15)
    ano     = models.IntegerField(verbose_name=_('Ano'))
    duracao = models.IntegerField(verbose_name=_(u'Duração'))
    preco   = models.FloatField(verbose_name=_(u'Preço'))
    user    = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        return reverse('dvd:detail', kwargs={'pk': self.pk}) 

    def __str__(self):
        ano = str(self.ano)  
        duracao = str(self.duracao)
        return self.titulo + ', ' + self.genero + ', ' + ano + ', ' + duracao