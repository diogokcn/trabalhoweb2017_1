from django.db import models

class JogoEletronico(models.Model):
    titulo       = models.CharField(max_length=50)
    estudio      = models.CharField(max_length=20)
    distribuidor = models.CharField(max_length=20)
    genero       = models.CharField(max_length=10)
    ano          = models.IntegerField()
    preco        = models.FloatField()
