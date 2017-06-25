from django.db import models

class Livro(models.Model):
    titulo  = models.CharField(max_length=100)
    ano     = models.IntegerField()
    editora = models.CharField(max_length=20)
    autora  = models.CharField(max_length=30)
    nroPags = models.IntegerField()
    formato = models.CharField(max_length=20)
    preco   = models.FloatField()
    
    # Representação do objeto em string
    def __str__(self):
        ano = str(self.ano)  
        return self.titulo + ', ' + self.autora + ', ' + ano + ', ' + self.editora
