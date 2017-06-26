from django.db import models

class Camiseta(models.Model):
    marca   = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=10)
    cor     = models.CharField(max_length=10)
    tecido  = models.CharField(max_length=30)   
    preco   = models.FloatField()

    def __str__(self):
        return self.marca + ', ' + self.tamanho + ', ' + self.cor + ', ' + self.tecido