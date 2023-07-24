from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tenis (models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='tenisimg/')

    def __str__(self):
        return self.nome