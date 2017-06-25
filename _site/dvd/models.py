from django.db import models

class DVD(models.Model):
    titulo  = models.CharField(max_length=50)
    genero  = models.CharField(max_length=15)
    ano     = models.IntegerField()
    duracao = models.IntegerField()
    preco   = models.FloatField()
